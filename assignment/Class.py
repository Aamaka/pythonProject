from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


p1 = Person("ade", 88)
p2 = Person("ade", 88)
print(p1 == p2)
