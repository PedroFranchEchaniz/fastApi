from fastapi import FastAPI
from pydantic import BaseModel
from School import School
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from Student import Student


app = FastAPI()

school = []

@app.post("/alumno", response_model=School, status_code=HTTP_201_CREATED)
async def createStuden(student: Student) -> School:
    school.student.append(student)
    return student

@app.get("/school", response_model=School, status_code=HTTP_200_OK)
async def getAll():
    return school




