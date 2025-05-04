from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlmodel import Session

from db import init_db, get_session
from models import StudentEntity
from service import update_survey, create_survey, delete_survey, get_student_survey, get_surveys


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan= lifespan)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Survey API!"}

@app.get("/api/survey/all")
def get_all_surveys(session: Session = Depends(get_session)):
    return get_surveys(session)

@app.post("/api/survey/create")
def create_student_survey( student: StudentEntity, session: Session = Depends(get_session)):
    return create_survey(student, session)


@app.patch("/api/survey/update/{student_id}")
def update_student_survey(student_id: int, student: StudentEntity, session: Session = Depends(get_session)):
   return update_survey(student_id, student, session)


@app.delete("/api/survey/delete/{student_id}")
def delete_student_survey(student_id: int, session: Session = Depends(get_session)):
   return delete_survey(student_id, session)

@app.get("/api/survey/{student_id}")
def get_student_survey(student_id: int, session: Session = Depends(get_session)):
    return get_student_survey(student_id, session)
