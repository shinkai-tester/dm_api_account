from __future__ import annotations
from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ConfigDict
from dm_api_account.models.rating import Rating
from dm_api_account.models.roles import UserRole


class User(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: Optional[StrictStr] = Field(None, description='Login')
    roles: Optional[List[UserRole]] = Field(None, description='Roles')
    medium_picture_url: Optional[StrictStr] = Field(
        None, alias='mediumPictureUrl', description='Profile picture URL M-size'
    )
    small_picture_url: Optional[StrictStr] = Field(
        None, alias='smallPictureUrl', description='Profile picture URL S-size'
    )
    status: Optional[StrictStr] = Field(None, description='User defined status')
    rating: Optional[Rating] = None
    online: Optional[datetime] = Field(None, description='Last seen online moment')
    name: Optional[StrictStr] = Field(None, description='User real name')
    location: Optional[StrictStr] = Field(None, description='User real location')
    registration: Optional[datetime] = Field(
        None, description='User registration moment'
    )


class UserEnvelope(BaseModel):
    model_config = ConfigDict(extra='forbid')

    resource: Optional[User] = None
    metadata: Optional[Any] = Field(None, description='Additional metadata')
