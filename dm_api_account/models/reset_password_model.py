from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ConfigDict


class ResetPassword(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
