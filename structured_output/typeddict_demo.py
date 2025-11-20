from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    
new_person: Person = {
    "name": "Alice",  # programmer knows upon hovering that 'name' is of type str
    "age": 30
}