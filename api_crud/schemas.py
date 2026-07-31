from typing import Optional

from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[str] = None


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True
