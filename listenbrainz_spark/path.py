import os

# Location new parquet dump listen files
LISTENBRAINZ_NEW_DATA_DIRECTORY = os.path.join('/', 'data', 'listenbrainz-new')

LISTENBRAINZ_INTERMEDIATE_STATS_DIRECTORY = os.path.join('/', 'data', 'stats-new')

LISTENBRAINZ_BASE_STATS_DIRECTORY = os.path.join('/', 'stats')
LISTENBRAINZ_SITEWIDE_STATS_DIRECTORY = os.path.join(LISTENBRAINZ_BASE_STATS_DIRECTORY, 'sitewide')
LISTENBRAINZ_USER_STATS_DIRECTORY = os.path.join(LISTENBRAINZ_SITEWIDE_STATS_DIRECTORY, 'user')

# MLHD+ dump files
MLHD_PLUS_RAW_DATA_DIRECTORY = os.path.join("/", "mlhd-raw")
MLHD_PLUS_DATA_DIRECTORY = os.path.join("/", "mlhd")  # processed MLHD+ dump data

# path to save incremental dumps
INCREMENTAL_DUMPS_SAVE_PATH = os.path.join(LISTENBRAINZ_NEW_DATA_DIRECTORY, "incremental.parquet")

# Directory containing RDD checkpoints to break lineage while using iterative algorithms.
CHECKPOINT_DIR = os.path.join('/', 'checkpoint')

################################################
# Recommendation `recording` absolute path/dir #
################################################

# Parent directory containing data used in and generated by `recording` recommendation engine.
RECOMMENDATION_RECORDING_PARENT_DIR = os.path.join('/', 'recommendation')
# Directory containing dataframes to be used in generating `recording` recommendations (not necessarily).
RECOMMENDATION_RECORDING_DATAFRAME_DIR = os.path.join(
    RECOMMENDATION_RECORDING_PARENT_DIR, 'dataframe')
# Directory containing model metadata and the real models to be used for generating `recording` recommendations.
RECOMMENDATION_RECORDING_MODEL_DIR = os.path.join(
    RECOMMENDATION_RECORDING_PARENT_DIR, 'model')
# Directory to save best models for `recording` recommendations.
RECOMMENDATION_RECORDING_DATA_DIR = os.path.join(
    RECOMMENDATION_RECORDING_MODEL_DIR, 'data')

RECORDING_SIMILARITY = "/data/recording-similarity"

RECORDING_DISCOVERY = os.path.join(RECOMMENDATION_RECORDING_PARENT_DIR, 'discovery')
RAW_RECOMMENDATIONS = os.path.join(RECOMMENDATION_RECORDING_PARENT_DIR, 'raw')

# Absolute path to dataframes used in processing raw data/listens for `recording` recommendations.
RECOMMENDATION_RECORDING_USERS_DATAFRAME = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'users_df.parquet'
RECOMMENDATION_RECORDINGS_DATAFRAME = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'recordings_df.parquet'
# Absolute path to processed data/listens ready to be trained for `recording` recommendations.
RECOMMENDATION_RECORDING_TRANSFORMED_LISTENCOUNTS_DATAFRAME = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'transformed_listencounts_df.parquet'
# Absolute path to model metadata.
RECOMMENDATION_RECORDING_MODEL_METADATA = RECOMMENDATION_RECORDING_MODEL_DIR + \
    '/' + 'model_metadata_new.parquet'
# Absolute path to mapped listens.
RECOMMENDATION_RECORDING_MAPPED_LISTENS = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'mapped_listens_df.parquet'
# Absolute path to save dataframe metadata
RECOMMENDATION_RECORDING_DATAFRAME_METADATA = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'dataframe_metadata.parquet'

#######################################################
# All the paths/dirs for `recording` recommendations  #
# should be contained within this block               #
#######################################################

# Absolute path to save import metadata
IMPORT_METADATA = "/import_metadata.parquet"

# Path to files downloaded from FTP.
FTP_FILES_PATH = '/rec/listenbrainz_spark'

###########################################
# paths/dirs used by user similarity jobs #
###########################################
USER_SIMILARITY_PARENT_DIR = os.path.join('/', 'user_similarity')
USER_SIMILARITY_DATAFRAME_DIR = os.path.join(
    USER_SIMILARITY_PARENT_DIR, 'dataframe')
USER_SIMILARITY_PLAYCOUNTS_DATAFRAME = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'playcounts_df.parquet')
USER_SIMILARITY_USERS_DATAFRAME = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'users_df.parquet')
USER_SIMILARITY_RECORDINGS_DATAFRAME = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'recordings_df.parquet')
USER_SIMILARITY_METADATA_DATAFRAME = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'dataframe_metadata.parquet')
USER_SIMILARITY_MAPPED_LISTENS = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'mapped_listens_df.parquet')

# MusicBrainz Release JSON dump
MUSICBRAINZ_RELEASE_DUMP = "/musicbrainz/release"
MUSICBRAINZ_RELEASE_DUMP_JSON_FILE = "/musicbrainz/release/mbdump/release"

# Release colors
RELEASE_COLOR_DUMP = "/release_color.json"

RELEASE_METADATA_CACHE_DATAFRAME = "/release_metadata_cache"
RELEASE_GROUP_METADATA_CACHE_DATAFRAME = "/release_group_metadata_cache"
ARTIST_COUNTRY_CODE_DATAFRAME = "/artist_country_code"
RECORDING_LENGTH_DATAFRAME = "/recording_length"
RECORDING_ARTIST_DATAFRAME = "/recording_artist"
ARTIST_CREDIT_MBID_DATAFRAME = "/artist_credit_mbid"
RECORDING_FEEDBACK_DATAFRAME = "/recording_feedback"
RECORDING_RECORDING_TAG_DATAFRAME = "/recording_tag"
RECORDING_ARTIST_TAG_DATAFRAME = "/artist_tag"
RECORDING_RELEASE_GROUP_TAG_DATAFRAME = "/release_group_tag"
RECORDING_RECORDING_GENRE_DATAFRAME = "/recording_genre"
RECORDING_ARTIST_GENRE_DATAFRAME = "/artist_genre"
RECORDING_RELEASE_GROUP_GENRE_DATAFRAME = "/release_group_genre"

MLHD_RECORDING_POPULARITY_DATAFRAME = "/mlhd_popularity_recording"
