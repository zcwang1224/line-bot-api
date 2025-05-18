from typing import Any
from pydantic import BaseModel, Field


class LineUserCreateModel(BaseModel):
    line_user_id: Any = Field(None, title="Line UserId")