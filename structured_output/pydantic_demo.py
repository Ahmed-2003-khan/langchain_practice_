from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str = 'Ahmed'
    age: Optional[int] = None


new_student = {'age':'22'}

student = Student(**new_student)

print(student)
