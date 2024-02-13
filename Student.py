from pydantic import BaseModel
from uuid import UUID, uuid4
from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Student(Base):

    id = Column(UUID, primary_key=True, index=True)
    name: Column(String)
    age: Column(Integer)

    class Config:
        from_attributes = True
