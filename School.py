from typing import List
from pydantic import BaseModel
from Student import Student  # Asegúrate de que la ruta de importación sea correcta

class School(BaseModel):
    students: List[Student] = []