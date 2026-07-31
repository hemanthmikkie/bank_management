from sqlalchemy.orm import Session
import models
import schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())  #creating a new student record
    db.add(db_student) #adding the student to existing table
    db.commit()  # committing the changes to db
    db.refresh(db_student)  #refreshing to fetch the updated table
    return db_student  #sending the response to user

def get_students(db: Session):
    return db.query(models.Student).all()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()


def get_by_course(db:Session,course_name:str):
    return db.query(models.Student).filter(models.Student.course==course_name).all()

def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = get_student(db, student_id)
    if not db_student:
        return None
    db_student.name = student.name
    db_student.age = student.age
    db_student.course = student.course
    db_student.email=student.email
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if not db_student:
        return None
    db.delete(db_student)
    db.commit()
    return db_student