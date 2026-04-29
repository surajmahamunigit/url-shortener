from pydantic import BaseModel, Field, HttpUrl
from pydantic import ConfigDict


class LickCreate(BaseModel):
    """
    Defines the shape of data expected when a user creates a short link.
    """

    # original_url must be valid URL
    original_url: HttpUrl


class LinkResponse(BaseModel):
    """ "
    Defines the shape of the data returned when link data is sent back to the client.
    """

    model_cofig = ConfigDict(from_attributes=True)

    id: int
    orginal_url: str
    short_url: str
    user_id: int


class StatsResponse(BaseModel):
    """
    Defines the shape of the data returned for the link statastics
    """

    mode_cofig = ConfigDict(from_attributes=True)

    short_code: str
    orgininal_url: str
    click_count: int
