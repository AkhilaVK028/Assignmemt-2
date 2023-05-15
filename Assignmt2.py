
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
myDB = db.AKHILA_V_K

app = FastAPI()

class Student(BaseModel):
    name:str
    roll:int
    course:str



@app.get("/")
def home():
    return {"This is for student registration into a course."}

@app.get("/show_details") #{shows the data of courses and the student enrolled}
def show():
    result = list(myDB.find({}))
    final_list = []
    for stud in result:
        del stud["_id"]
        final_list.append(stud)
    return {"The data for all students ": final_list}

@app.post("/add")
def add(student:Student):
    if list(myDB.find({"roll":student.roll})) == []:
     myDB.insert_one(student.dict())
     return {"Success":"Added student in the course successfully"}
    else:
            return {"Error":"Cannot add student, already enrolled in a course"}


@app.put("/update/{roll}")
def update(roll:int,student: Student):
    if list(myDB.find({"roll":roll})) == []:
        return {"Error":"Student not enrolled in any course"}
    else:
     myDB.update_one({"roll":roll},{"$set":student.dict()})
     return {"Success":"Updated succesfully"}

@app.delete("/delete/{roll}")
def delete(roll:int):
  if list(myDB.find({"roll":roll})) == []:
        return {"Error":"Student has not enrolled in any course till now"}
# del course_details["roll"]
  myDB.delete_one({"roll":roll})
  return {"Success":"Deleted the student from the course"}
