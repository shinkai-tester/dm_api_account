from typing import Optional
from pydantic import StrictStr, BaseModel, Field, ConfigDict


class GeneralError(BaseModel):
    model_config = ConfigDict(extra='forbid')

    message: Optional[StrictStr] = Field(None, description='Client message')
