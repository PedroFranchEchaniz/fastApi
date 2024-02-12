from pydantic import BaseModel
from uuid import UUID, uuid4


class Student(BaseModel):
    id: UUID = None
    name: str
    age: int

    def __init__(__pydantic_self__, **data):
        if 'id' not in data:
            data['id'] = uuid4()
        super().__init__(**data)