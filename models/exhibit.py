from typing import Any
from pydantic import BaseModel, Field

# region Exhibit Model

class ExhibitCreateModel(BaseModel):
    ex_name: Any = Field(None)
    county: Any = Field(None)
    address: Any = Field(None)    
    lng: Any = Field(None)
    lat: Any = Field(None)
    pic_url: Any = Field(None)
    klook_url: Any = Field(None)
    s_time: Any = Field(None)
    e_time: Any = Field(None)
    
# endregion Exhibit Model