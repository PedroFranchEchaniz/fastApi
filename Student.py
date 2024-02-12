from pydantic import  Field
from pydantic import BaseModel
from uuid import uuid4

class Student (BaseModel):

    id: uuid4()
    name: str
    age: int