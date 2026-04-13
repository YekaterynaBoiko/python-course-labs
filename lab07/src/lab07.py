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
# Testing
# ====================

# Task A
print("A) Regular class (duck typing)")
student = StudentRegular("Yekateryna Boiko", "КН-124", 94.3)
export(student)

print("\n" + "-"*40 + "\n")

# Task B
print("B) Dataclass implementation")
student_taskB = StudentData("Vasya", "ПМ-100", 63.9)
export(student_taskB)

print("\n" + "-"*40 + "\n")

# Task C
print("C) Slots")
student_taskC = StudentSlots("Bob", "A-190", 75.4)
export(student_taskC)

print("\n" + "-"*40 + "\n")

# Task D
print("D) ABC version")
student_taskD = StudentABC("Anton", "E-55", 87.2)
print(student_taskD.serialize())
export(student_taskD)
