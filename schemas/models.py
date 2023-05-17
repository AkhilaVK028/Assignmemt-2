from pydantic import BaseModel


class Student(BaseModel):
    name: str
    roll: int
    course: str
    fees: int


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str