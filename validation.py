def validate_marks(marks, maximum_marks=100):
    if marks < 0:
        return False, "Marks cannot be negative."

    if marks > maximum_marks:
        return False, f"Marks cannot be greater than {maximum_marks}."

    return True, "Valid marks."


def validate_attendance(attendance):
    if attendance < 0 or attendance > 100:
        return False, "Attendance must be between 0 and 100."

    return True, "Valid attendance."


def validate_income(income):
    if income < 0:
        return False, "Family income cannot be negative."

    return True, "Valid family income."


def validate_number_of_subjects(number):
    if number <= 0:
        return False, "Number of subjects must be greater than 0."

    return True, "Valid number of subjects."