from typing import Any
from pydantic import BaseModel, Field

# region Exhibit Model

class MongodbUserModel(BaseModel):
    _id: Any = Field(None)
    user_id: Any = Field(None, description="")
    area: Any = Field(None, description="ex. 北區")
    county: Any = Field(None, description="ex. 台北市")
    township: Any = Field(None, description="ex. 中山區")
    s_type: Any = Field(None, description="ex. 找附近 找活動 找展演")
    s_cate: Any = Field(None, description="")
    s_detail: Any = Field(None, description="")
    s_type_url: Any = Field(None, description="")
    s_detail_url: Any = Field(None, description="")
    c_time: Any = Field(None, description="")
    
# endregion Exhibit Model