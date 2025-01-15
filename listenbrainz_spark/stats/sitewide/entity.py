import logging
from typing import Dict, Iterator

from listenbrainz_spark.stats import SITEWIDE_STATS_ENTITY_LIMIT
from listenbrainz_spark.stats.incremental.aggregator import Aggregator
from listenbrainz_spark.stats.incremental.range_selector import StatsRangeListenRangeSelector
from listenbrainz_spark.stats.incremental.sitewide.artist import AritstSitewideEntity
from listenbrainz_spark.stats.incremental.sitewide.entity import SitewideEntityProvider, \
    SitewideEntityStatsMessageCreator
from listenbrainz_spark.stats.incremental.sitewide.recording import RecordingSitewideEntity
from listenbrainz_spark.stats.incremental.sitewide.release import ReleaseSitewideEntity
from listenbrainz_spark.stats.incremental.sitewide.release_group import ReleaseGroupSitewideEntity

logger = logging.getLogger(__name__)

incremental_sitewide_map: Dict[str, type[SitewideEntityProvider]] = {
    "artists": AritstSitewideEntity,
    "releases": ReleaseSitewideEntity,
    "recordings": RecordingSitewideEntity,
    "release_groups": ReleaseGroupSitewideEntity,
}


def get_entity_stats(entity: str, stats_range: str) -> Iterator[Dict]:
    """ Returns top entity stats for given time period """
    logger.debug(f"Calculating sitewide_{entity}_{stats_range}...")
    selector = StatsRangeListenRangeSelector(stats_range)
    entity_cls = incremental_sitewide_map[entity]
    entity_obj: SitewideEntityProvider = entity_cls(selector, SITEWIDE_STATS_ENTITY_LIMIT)
    message_creator = SitewideEntityStatsMessageCreator(entity, selector)

    aggregator = Aggregator(entity_obj, message_creator)
    return aggregator.main()
