from pydantic import BaseModel, ConfigDict, Field
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "FastAPI Book Launch",
                "image": "https://example.com/image.png",
                "description": "Discussion about FastAPI",
                "tags": [
                    "python",
                    "fastapi",
                    "book"
                ],
                "location": "Google Meet"
            }
        }
    )
