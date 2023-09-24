from typing import List, Dict, Optional
from pydantic import StrictStr, BaseModel, Field, ConfigDict


class BadRequestError(BaseModel):
    model_config = ConfigDict(extra='forbid')

    message: Optional[StrictStr] = Field(None, description='Client message')
    invalid_properties: Optional[Dict[str, List[StrictStr]]] = Field(
        None,
        alias='invalidProperties',
        description='Key-value pairs of invalid request properties',
    )
