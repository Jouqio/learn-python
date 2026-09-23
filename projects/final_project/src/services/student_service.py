"""Business logic for managing students: add, view, search, update, delete."""
from src.models.student import Student
from src.utils.validators import validate_name, validate_gpa, ValidationError


class StudentService:
    def __init__(self, repository):
        self.repository = repository
        self.students = [Student.from_dict(d) for d in self.repository.load_all()]

    def _save(self):
        self.repository.save_all([s.to_dict() for s in self.students])

    def _next_id(self):
        if not self.students:
            return 1
        return max(s.student_id for s in self.students) + 1

    def add_student(self, name, major, gpa=0.0):
        name = validate_name(name)
        gpa = validate_gpa(gpa)
        student = Student(self._next_id(), name, major, gpa)
        self.students.append(student)
        self._save()
        return student

    def list_students(self):
        return list(self.students)

    def find_student(self, name):
        matches = [s for s in self.students if s.name.lower() == name.lower()]
        return matches[0] if matches else None

    def update_student(self, student_id, **fields):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student is None:
            raise ValidationError(f"No student with id {student_id}")
        if "name" in fields:
            student.name = validate_name(fields["name"])
        if "major" in fields:
            student.major = fields["major"]
        if "gpa" in fields:
            student.gpa = validate_gpa(fields["gpa"])
        self._save()
        return student

    def delete_student(self, student_id):
        before = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        self._save()
        return len(self.students) < before
