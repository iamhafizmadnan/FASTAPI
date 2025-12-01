from fastapi import FastAPI, Path

app = FastAPI()

Students = ["Adnan", "Ali", "Ahsan", "Ahmed", "Asim", "Adeel", "Aftab", "Ammar","Bilal", "Basit", "Babar", "Bashir"]

@app.get("/")
def root():
    return "hello Adnan"

@app.get("/Students")
def get_students():
    return Students



@app.get("/Students")
def filter_students(sw: str):
    filtered_names = []
    sw = sw.casefold()
    for student in Students:
        if student.casefold().startswith(sw):
            filtered_names.append(student)
    return filtered_names


@app.get("/Students/{id}")
def get_student(id: int = Path(gt=0, le=len(Students))):
    return Students[id] 
