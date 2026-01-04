from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = 'Ahmed'
    age: Optional[int] = None
    email: EmailStr


new_student = {'age':'22', 'email':'abc'}

student = Student(**new_student)

print(student)
