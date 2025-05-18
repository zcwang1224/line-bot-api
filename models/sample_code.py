from typing import Any
from pydantic import BaseModel, Field

# region Redis Model

class SampleCodeRedisAddModel(BaseModel):
    line_user_id: Any = Field(None, title="Line UserId")
    lat: Any = Field(None, title="Latitude")
    lon: Any = Field(None, title="Longitude")
    area: Any = Field(None, title="Area")
    city: Any = Field(None, title="City")
    search_type: Any = Field(None, title="Search Type")
    
# endregion Redis Model

# region Sample Location Model

class SampleLocationAddModel(BaseModel):
    
    name: Any = Field(None, title="名稱")
    lat: Any = Field(None, title="經度")
    lng: Any = Field(None, title="緯度")
    
# endregion Sample Location Model

