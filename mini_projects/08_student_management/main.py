"""Mini Project 08: Student Management (mini version)"""


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student(name={self.name!r}, grade={self.grade})"


class StudentRegistry:
    def __init__(self):
        self.students = []

    def add(self, name, grade):
        self.students.append(Student(name, grade))

    def top_student(self):
        return max(self.students, key=lambda s: s.grade, default=None)


def main():
    registry = StudentRegistry()
    registry.add("Yusuf", 88)
    registry.add("Zahra", 95)
    print(registry.students)
    print("Top student:", registry.top_student())


if __name__ == "__main__":
    main()
