from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
myDB = db.AKHILA_V_K


class Student(BaseModel):
    name: str
    roll: int
    course: str
    fees: int
