from typing import List
from pydantic import BaseModel, EmailStr, ConfigDict, Field

from models.events import Event


class User(BaseModel):
    email: EmailStr
    username: str
    events: List[Event] = Field(default_factory=list)


class NewUser(User):
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "ilya@example.com",
                "username": "PashinIlya",
                "password": "Strong123!",
                "events": []
            }
        }
    )


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "ilya@example.com",
                "password": "Strong123!"
            }
        }
    )
