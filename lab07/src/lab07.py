from typing import Protocol
from dataclasses import dataclass
from abc import ABC, abstractmethod

class Serializable(Protocol):
    def serialize(self) -> str:
        ...

def export(obj: Serializable) -> None:
    print(obj.serialize())


class StudentRegular:
    def __init__(self, name: str, group: str, average_grade: float):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    # Task A
    def serialize(self) -> str:
        return f"Student(name={self.name}, group={self.group}, average_grade={self.average_grade})"

# Task B
@dataclass
class StudentData:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"Student(name={self.name}, group={self.group}, average_grade={self.average_grade})"

# Task C
@dataclass(slots=True)
class StudentSlots:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"Student(name={self.name}, group={self.group}, average_grade={self.average_grade})"

# Task D
class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

class StudentABC(SerializableABC):
    def __init__(self, name: str, group: str, average_grade: float):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"Student(name={self.name}, group={self.group}, average_grade={self.average_grade})"

# ====================
# Students datasource
# ====================

students_data_source = [
    ("Yekateryna Boiko", "КН-124", 94.3),
    ("Sofia Lytvynenko", "КН-124", 100.0),
    ("Maryna Hysachenko", "ІПЗ-121", 88.7),
    ("Vasya Petrenko", "Е-100", 63.4),
    ("Mariia Kovalenko", "ПМ-211", 72.1)
]

# ====================
# Testing
# ====================

# Task A
print("A) Regular class (duck typing)")
for name, group, average_grade in students_data_source:
    student = StudentRegular(name, group, average_grade)
    export(student)

print("\n" + "-"*40 + "\n")

# Task B
print("B) Dataclass implementation")
for name, group, average_grade in students_data_source:
    student_taskB = StudentData(name, group, average_grade)
    export(student_taskB)

print("\n" + "-"*40 + "\n")

# Task C
print("C) Slots")
for name, group, average_grade in students_data_source:
    student_taskC = StudentSlots(name, group, average_grade)
    export(student_taskC)

print("\n" + "-"*40 + "\n")

# Task D
print("D) ABC version")
for name, group, average_grade in students_data_source:
    student_taskD = StudentABC(name, group, average_grade)
    print(student_taskD.serialize()) # The line is drawn again when called
    export(student_taskD)
