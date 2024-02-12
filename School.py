from typing import List
from pydantic import BaseModel

import Student

class School (BaseModel):
    students: List [Student]
