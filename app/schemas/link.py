from pydantic import BaseModel, HttpUrl
from pydantic import ConfigDict


class LinkCreate(BaseModel):
    """
    Defines the shape of data expected when a user creates a short link.
    """

    original_url: HttpUrl


class LinkResponse(BaseModel):
    """
    Defines the shape of data returned when link data is sent back to the client.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    original_url: str
    short_code: str
    click_count: int
    user_id: int


class StatsResponse(BaseModel):
    """
    Defines the shape of data returned for link statistics.
    """

    model_config = ConfigDict(from_attributes=True)

    short_code: str
    original_url: str
    click_count: int
