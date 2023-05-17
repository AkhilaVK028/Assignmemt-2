from scripts.utility.mongo_utility import myDB, Student



def home():
    return {"This is for student registration into a course."}


def get_student():
    result = list(myDB.find({}))
    final_list = []
    for stud in result:
        del stud["_id"]
        final_list.append(stud)
    return {"The data for all students ": final_list}


def insert_student(student: Student):
    if not list(myDB.find({"roll": student.roll})):
        myDB.insert_one(student.dict())
        return {"Success": "Added student in the course successfully"}
    else:
        return {"Error": "Cannot add student, already enrolled in a course"}


def update_student(roll: int, student: Student):
    if not list(myDB.find({"roll": roll})):
        return {"Error": "Student not enrolled in any course"}
    else:
        myDB.update_one({"roll": roll}, {"$set": student.dict()})
        return {"Success": "Updated succesfully"}


def delete_student(roll: int):
    if not list(myDB.find({"roll": roll})):
        return {"Error": "Student has not enrolled in any course till now"}
    myDB.delete_one({"roll": roll})
    return {"Success": "Deleted the student from the course"}




def pipeline_agg():
    pipe = [
    {
        '$group': {
            '_id': None,
            'total_amount': {
                '$sum': '$fees'
            }
        }
    }, {
        '$project': {
            '_id': 0
        }
    }
]
    data = myDB.aggregate(pipe)
    data = list(data)
    print(data)
    return {"Total_fees_collected": (data)[0]['total_amount']}