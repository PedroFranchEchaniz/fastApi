from typing import Optional

from datetime import datetime
from pydantic import BaseModel, Field

class StudentDto(BaseModel):
    name: str = Field(...)
    age: Optional[int] = Field(None)

    class Config:
        from_attributes = True