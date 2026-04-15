from typing import List, Iterator, Optional, Type, Any, Literal
# Task C

class GradeValidator:
    def __set_name__(self, owner: Type[object], name: str) -> None:
        self.name = name

    def __get__(self, instance: object, owner: type) -> Any:
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance: object, value: float) -> None:
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        instance.__dict__[self.name] = value


class Student:
    grade = GradeValidator() # for task D

    def __init__(self, name: str, group: str, grade: float):
        self.name = name
        self.group = group
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.name} ({self.grade}) - {self.group}"

# Task A

class StudentIterator:
    def __init__(self, students: List[Student]) -> None:
        self._students: List[Student] = students
        self._index: int = 0

    def __iter__(self) -> "StudentIterator":
        return self

    def __next__(self) -> Student:
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        raise StopIteration


class StudentCollection:
    def __init__(self, students: Optional[List[Student]] = None) -> None:
        if students is None:
            self._students: List[Student] = []
        else:
            self._students = students

    def add_student_to_collection(self, student: Student) -> None:
        self._students.append(student)

    def __iter__(self) -> StudentIterator:
        return StudentIterator(self._students)

    # Task B
    def __enter__(self) -> "StudentCollection":
        print("Entering StudentCollection context")
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[object],
    ) -> Literal[False]:
        print("Exiting StudentCollection context")

        if exc_type:
            print(f"An error occurred: {exc_value}")

        return False


# ====================
# Testing
# ====================

# Students: dataSetup
student1 = Student("Yekateryna Boiko", "КН-124", 94.3)
student2 = Student("Sofia Lytvynenko", "КН-124", 100.0)
student3 = Student("Maryna Hysachenko", "ІПЗ-121", 88.7)


print("A) Iteration")

collection = StudentCollection()
collection.add_student_to_collection(student1)
collection.add_student_to_collection(student2)
collection.add_student_to_collection(student3)

for student in collection:
    print(student)

print("\n" + "-" * 40 + "\n")

print("B) Context Manager")

with StudentCollection() as collection:
    collection.add_student_to_collection(student1)
    collection.add_student_to_collection(student2)

    for student in collection:
        print(student)

print("\n" + "-" * 40 + "\n")

print("C) Descriptor")

student_taskC = Student("Mariia Kovalenko", "ПМ-211", 72.1)
print(student_taskC)

student_taskC.grade = 90
print(student_taskC)

try:
    student_taskC.grade = 120
except ValueError as e:
    print(f"Error: {e}") # The result hier is: Error: Grade must be between 0 and 100
    # because in line 116 we make student_taskC.grade = 120

print("\n" + "-" * 40 + "\n")

print("D) Integration")
students: List[Student] = [student1, student2, student3]

with StudentCollection(students) as collection:
    for student in collection:
        print(student.grade)