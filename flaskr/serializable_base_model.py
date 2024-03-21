from typing import Optional, Literal

from pydantic import BaseModel, NonNegativeInt, Field

from flaskr.api_input import Gender


class SerializableDefaultModel(BaseModel):
    class Config:
        use_enum_values = True

    def to_dict(self):
        return self.model_dump(by_alias=True)


class SomeOutput(SerializableDefaultModel):
    name: str
    age: NonNegativeInt
    acceptance: Optional[bool] = Field(False, serialization_alias="accepted")
    option: Optional[bool] = None
    gender: Gender
    preferences: Literal["yellow", "pink"]
