from typing import Optional, Literal

from pydantic import BaseModel, NonNegativeInt
from enum import Enum


class Gender(Enum):
    F = "f"
    M = "m"
    O = "o"


class SomeInput(BaseModel):
    name: str
    age: NonNegativeInt
    acceptance: Optional[bool]
    gender: Gender
    preferences: Literal["yellow", "pink"]

    class Config:
        use_enum_values = True
