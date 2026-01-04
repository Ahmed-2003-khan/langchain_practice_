from pydantic import BaseModel

class Student(BaseModel):
    name: str


new_student = {'name':'ahmed'}

student = Student(**new_student)

print(student)
