from typing import Any
from pydantic import BaseModel, Field

# region Exhibit Model

class AccomoCreateModel(BaseModel):
    a_name: Any = Field(None)
    b_hours: Any = Field(None)
    county: Any = Field(None)
    address: Any = Field(None)
    rate: Any = Field(None)
    lng: Any = Field(None)
    lat: Any = Field(None)
    pic_url: Any = Field(None)
    b_url: Any = Field(None)
    ac_type: Any = Field(None)
    comm: Any = Field(None)
    area: Any = Field(None)
    
# endregion Exhibit Model