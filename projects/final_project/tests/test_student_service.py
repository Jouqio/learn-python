"""Basic pytest tests for the Student Management System's service layer."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.repositories.json_repository import JSONStudentRepository
from src.services.student_service import StudentService
from src.utils.validators import ValidationError
import pytest


@pytest.fixture
def service(tmp_path):
    repo = JSONStudentRepository(filepath=str(tmp_path / "students.json"))
    return StudentService(repo)


def test_add_student(service):
    student = service.add_student("Test Name", "Informatics", 3.5)
    assert student.name == "Test Name"
    assert len(service.list_students()) == 1


def test_add_student_invalid_gpa(service):
    with pytest.raises(ValidationError):
        service.add_student("Test Name", "Informatics", 5.0)


def test_find_student(service):
    service.add_student("Rina", "Informatics", 3.5)
    found = service.find_student("rina")
    assert found is not None
    assert found.name == "Rina"


def test_update_student(service):
    student = service.add_student("Rina", "Informatics", 3.5)
    updated = service.update_student(student.student_id, gpa=3.9)
    assert updated.gpa == 3.9


def test_delete_student(service):
    student = service.add_student("Rina", "Informatics", 3.5)
    assert service.delete_student(student.student_id) is True
    assert service.list_students() == []
