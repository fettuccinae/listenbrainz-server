from pydantic import BaseModel, constr, validator
from data.model.validators import check_valid_uuid

from typing import Optional, List


class RecordingRecord(BaseModel):
    """ Each individual record for a user's recording stats
    """
    artist_name: constr(min_length=1)
    artist_mbids: List[constr(min_length=1)] = []
    recording_mbid: Optional[str]
    release_name: Optional[str]
    release_mbid: Optional[str]
    track_name: str
    listen_count: int
    # to add empty fields to stats API response, for compatibility
    artist_msid: Optional[str]
    recording_msid: Optional[str]
    release_msid: Optional[str]

    _validate_uuids: classmethod = validator(
        "recording_mbid",
        "release_mbid",
        allow_reuse=True
    )(check_valid_uuid)

    _validate_artist_mbids: classmethod = validator("artist_mbids", each_item=True, allow_reuse=True)(check_valid_uuid)

