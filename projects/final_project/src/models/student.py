"""Student model: plain data + simple validation-free representation."""


class Student:
    def __init__(self, student_id, name, major, gpa=0.0):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "major": self.major,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            major=data["major"],
            gpa=data.get("gpa", 0.0),
        )

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.major}, gpa={self.gpa})"
