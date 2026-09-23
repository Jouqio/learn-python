"""Input validation helpers used across the Student Management System."""


class ValidationError(Exception):
    """Raised when user-provided data fails validation."""


def validate_name(name):
    if not name or not name.strip():
        raise ValidationError("Name cannot be empty.")
    return name.strip()


def validate_gpa(gpa):
    try:
        gpa_value = float(gpa)
    except (TypeError, ValueError):
        raise ValidationError("GPA must be a number.")
    if not (0.0 <= gpa_value <= 4.0):
        raise ValidationError("GPA must be between 0.0 and 4.0.")
    return gpa_value
