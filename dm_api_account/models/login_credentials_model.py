from typing import Optional
from pydantic import BaseModel, StrictStr, Field, ConfigDict


class LoginCredentials(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    remember_me: Optional[bool] = Field(None, alias='rememberMe')
