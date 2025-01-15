import abc
import logging

from listenbrainz_spark.path import LISTENBRAINZ_LISTENER_STATS_DIRECTORY
from listenbrainz_spark.stats.incremental.user.entity import UserEntityProvider, UserStatsMessageCreator

logger = logging.getLogger(__name__)


class EntityListener(UserEntityProvider, abc.ABC):
    """ See base class IncrementalStats for documentation. """

    def get_table_prefix(self) -> str:
        return f"{self.entity}_listener_{self.stats_range}"

    def get_base_path(self) -> str:
        return LISTENBRAINZ_LISTENER_STATS_DIRECTORY

    def get_entity_id(self):
        raise NotImplementedError()


class EntityStatsMessageCreator(UserStatsMessageCreator):

    def items_per_message(self):
        return 10000
