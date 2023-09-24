from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class Rating(BaseModel):
    model_config = ConfigDict(extra='forbid')

    enabled: Optional[bool] = Field(None, description='Rating participation flag')
    quality: Optional[int] = Field(None, description='Quality rating')
    quantity: Optional[int] = Field(None, description='Quantity rating')
