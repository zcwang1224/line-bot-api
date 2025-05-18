from typing import Any
from pydantic import BaseModel, Field

# region Line Bot Postback Data

class PostbackDataModel(BaseModel):
    menu_type: Any = Field(None, title="Line Bot 選單項目，ex. 找展演")
    area: Any = Field(None, title="區域")
    county: Any = Field(None, title="縣市")
    district: Any = Field(None, title="鄉鎮區")
    main_type: Any = Field(None, title="")
    lat: Any = Field(None, title="")
    lng: Any = Field(None, title="")
    sub_type: Any = Field(None, title="")
    trigger_type: Any = Field(None, title="")
    address: Any = Field(None, title="")
    
# endregion Line Bot Postback Data

if __name__ == "__main__":
    data = PostbackDataModel(
        menu_type=1,
        lng=23.0001
    )
    import json
    print(data.model_dump_json())