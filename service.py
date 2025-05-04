
from fastapi import HTTPException
from sqlmodel import Session, select

from models import StudentEntity


def update_survey(student_id: int, student: StudentEntity, session: Session):
    try:
        existing_student = session.get(StudentEntity, student_id)
        if not existing_student:
            return {"message": "Student not found"}

        updated_student = update_student_model(existing_student, student)

        session.add(updated_student)
        session.commit()
        session.refresh(updated_student)

        return {"message": "Student survey updated successfully", "student": updated_student}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()

def update_student_model(student, data):
    student.first_name = data.first_name
    student.last_name = data.last_name
    student.street_address = data.street_address
    student.city = data.city
    student.state = data.state
    student.zip = data.zip
    student.phone_number = data.phone_number
    student.email = data.email
    student.date_of_survey = data.date_of_survey
    student.liked_most = data.liked_most
    student.interest_source = data.interest_source
    student.recommend_likelihood = data.recommend_likelihood
    return student

def create_survey( student: StudentEntity, session: Session):
    student = StudentEntity(
        first_name=student.first_name,
        last_name=student.last_name,
        street_address=student.street_address,
        city=student.city,
        state=student.state,
        zip=student.zip,
        phone_number=student.phone_number,
        email=student.email,
        date_of_survey=student.date_of_survey,
        liked_most=student.liked_most,
        interest_source=student.interest_source,
        recommend_likelihood=student.recommend_likelihood
    )
    try:
        session.add(student)
        session.commit()
        session.refresh(student)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
    return {"message": "Student survey submitted successfully","student": student}

def delete_survey(student_id: int, session: Session):
    try:
        existing_student = session.get(StudentEntity, student_id)
        if not existing_student:
            return {"message": "Student survey not found"}

        session.delete(existing_student)
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
    return {"message": "Student survey deleted successfully"}

def get_student_survey(student_id: int, session: Session):
    try:
        existing_student = session.get(StudentEntity, student_id)
        if not existing_student:
            raise HTTPException(status_code=404, detail="Student survey not found")
        return {"student_survey": existing_student}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()

def get_surveys(session: Session):
    try:
       students = session.exec(select(StudentEntity)).all()
       return {"student_surveys": students}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()