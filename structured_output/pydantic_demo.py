from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Ahmed'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0.0, lt=4.0)


new_student = {'age':'22', 'email':'abc@gmail.com', 'cgpa':5}

student = Student(**new_student)

print(student)
