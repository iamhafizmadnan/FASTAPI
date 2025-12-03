from typing import Optional
from fastapi import FastAPI , Body, Query  ,Form

app = FastAPI()

students = [
    {"id": 1, "name": "Alice","math": 85, "science": 90, "english": 88},
    {"id": 2, "name": "Bob","math": 78, "science": 82, "english": 80},
    {"id": 3, "name": "Charlie","math": 92, "science": 88, "english": 91},
    {"id": 4, "name": "David","math": 65, "science": 70, "english": 72},
    {"id": 5, "name": "Eva","math": 90, "science": 95, "english": 94},
    {"id": 6, "name": "Frank","math": 75, "science": 80, "english": 78}
    
]

@app.get("/")
def root():
    return {"message": "Student marksheet API"}

@app.post("/myname")
def my_name(name:str = Body(..., embed=True)):
    return {"message": f"Hello, {name}!"}


@app.get("/students")
def get_students(limit: Optional[int] = None):
    if limit is not None:
        return students[:limit]
    return students

# @app.post("/add_student")
# def add_student(payload: dict = Body(...)):
#     students.append(payload)
#     return {"message": "Student added successfully", "student": payload}



@app.post("/add_student")
def add_student(
    id: int = Form(...),
    name: str = Form(...),
    math: int = Form(...),
    science: int = Form(...),
    english: int = Form(...)
):
    payload = dict(
        id=id,
        name=name,
        math=math,
        science=science,
        english=english
)
    students.append(payload)
    return {"message": "Student added successfully", "student": payload}


@app.get("/students/{id}")
def get_student(id :int):
    
    found_student = None
    for student in students:
        if student ['id'] == id:
                    found_student = student
                    break
    if found_student is None:
        return {"message": "Student not found"}
        
    subjects = ['math', 'science', 'english']
    total_marks = 100 * len(subjects)
    obtained_marks = 0
    
    for sub in subjects:
        obtained_marks += found_student[sub]
     
    perctentage = round(obtained_marks / total_marks * 100,2) 
    result = "Pass" if perctentage >= 40 else "Fail"
    
    response = {
        "ID": found_student['id'],
        "Name": found_student['name'],
        "Total Marks": total_marks, 
         "MARKS": {sub: found_student[sub] for sub  in subjects},
        "Obtained Marks": obtained_marks,
        "Percentage": perctentage,
        "Result": result
    }