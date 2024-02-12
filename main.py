from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from School import School
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from Student import Student
from uuid import UUID


app = FastAPI()

school = School()


@app.post("/alumno", response_model=Student, status_code=HTTP_201_CREATED)
async def createStuden(student: Student) -> Student:
    school.students.append(student)
    return student


@app.get("/school", response_model=School, status_code=HTTP_200_OK)
async def getAll():
    return school


@app.get("/alumno/{id}", response_model=Student, status_code=HTTP_200_OK)
async def get_student(id:UUID):
    for student in school.students:
        if student.id == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.put("/alumno/{id}", response_model=Student, status_code=HTTP_200_OK)
async def edit_student(id:UUID, edit_student:Student):
    for index, student in enumerate(school.students):
        if student.id == id:
            school.students[index] == edit_student
            return edit_student
        raise HTTPException(status_code=404, detail="Error editing")


