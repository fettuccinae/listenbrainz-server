import pycountry

import listenbrainz_spark
from listenbrainz_spark import config
from listenbrainz_spark.path import ARTIST_COUNTRY_CODE_DATAFRAME
from listenbrainz_spark.postgres.utils import load_from_db
from listenbrainz_spark.stats import run_query


def create_iso_country_codes_df():
    """ Create a dataframe mapping 2 letter iso codes to 3 letter iso country codes because
    MB stores the 2 letter iso code but the frontend needs the 3 letter iso code."""
    iso_codes = []
    for country in pycountry.countries:
        iso_codes.append((country.alpha_2, country.alpha_3))

    df = listenbrainz_spark.session.createDataFrame(iso_codes, schema=["alpha_2", "alpha_3"])
    df.createOrReplaceTempView("iso_codes")



def create_artist_country_cache():
    """ Import artist country from postgres to HDFS for use in artist map stats calculation. """
    query = """
        -- for the case where artist area is a subdivision of a country
        SELECT a.gid AS artist_mbid
             , a.name AS artist_name
             , iso.code AS country_code_alpha_2
          FROM musicbrainz.artist a
          JOIN musicbrainz.area_containment ac
            ON ac.descendant = a.area
          JOIN musicbrainz.iso_3166_1 iso
            ON iso.area = ac.parent
         UNION
         -- for the case where artist area is a country itself
        SELECT a.gid AS artist_mbid
             , a.name AS artist_name
             , iso.code AS country_code_alpha_2
          FROM musicbrainz.artist a
          JOIN musicbrainz.iso_3166_1 iso
            ON iso.area = a.area
        -- for the case where artist area is null
         UNION
        SELECT a.gid AS artist_mbid
             , a.name AS artist_name
             , NULL AS country_code_alpha_2
          FROM musicbrainz.artist a
         WHERE a.area IS NULL
    """
    artist_df = load_from_db(config.PG_JDBC_URI, config.PG_USER, config.PG_PASSWORD, query)
    artist_df.createOrReplaceTempView("artist_cache_mb_db")

    create_iso_country_codes_df()

    final_query = """
        SELECT artist_mbid
             , artist_name
             , alpha_3 AS country_code
          FROM artist_cache_mb_db
     LEFT JOIN iso_codes
            ON country_code_alpha_2 = alpha_2
    """
    run_query(final_query) \
        .write \
        .format("parquet") \
        .save(config.HDFS_CLUSTER_URI + ARTIST_COUNTRY_CODE_DATAFRAME, mode="overwrite")
