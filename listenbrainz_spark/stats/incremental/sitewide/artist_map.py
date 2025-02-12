from typing import List, Iterator, Dict

from pyspark.sql import DataFrame

from listenbrainz_spark.stats.incremental.message_creator import StatsMessageCreator
from listenbrainz_spark.stats.incremental.sitewide.artist import AritstSitewideEntity


class ArtistMapSitewideEntity(AritstSitewideEntity):
    """ See base class QueryProvider for details. """

    def get_stats_query(self, final_aggregate, cache_tables: List[str]):
        cache_table = cache_tables[0]
        return f"""
            WITH ranked_stats AS (
                SELECT artist_name
                     , artist_mbid
                     , listen_count
                  FROM {final_aggregate}
                 WHERE artist_mbid IS NOT NULL
              ORDER BY listen_count DESC
                 LIMIT {self.top_entity_limit}
            ), ranked_countries AS (
                SELECT country_code AS country
                     , count(*) as artist_count
                     , sum(listen_count) as listen_count
                     , sort_array(
                            collect_list(
                                struct(
                                    listen_count
                                  , rs.artist_name
                                  , rs.artist_mbid
                                )
                            )
                            , false
                       ) as artists
                  FROM ranked_stats rs
                  JOIN {cache_table}
                 USING (artist_mbid)
              GROUP BY country_code
            )
                SELECT sort_array(
                            collect_list(
                                struct(
                                    artist_count
                                  , listen_count
                                  , country
                                  , artists
                                )
                            )
                            , false
                       ) AS data
                  FROM ranked_countries
        """


class ArtistMapSitewideStatsMessageCreator(StatsMessageCreator):

    def __init__(self, selector):
        super().__init__("artist_map", "sitewide_entity", selector)

    @property
    def default_database_prefix(self):
        return ""

    def create_messages(self, results: DataFrame, only_inc: bool) -> Iterator[Dict]:
        entry = results.collect()[0].asDict(recursive=True)
        message = {
            "type": self.message_type,
            "stats_range": self.stats_range,
            "from_ts": int(self.from_date.timestamp()),
            "to_ts": int(self.to_date.timestamp()),
            "entity": self.entity,
            "data": entry["data"],
        }
        yield message
