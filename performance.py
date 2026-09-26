def calculate_total(subjects):
    return sum(subjects.values())


def calculate_percentage(subjects):
    total = calculate_total(subjects)
    maximum_marks = len(subjects) * 100
    percentage = (total / maximum_marks) * 100
    return percentage


def calculate_average(subjects):
    return sum(subjects.values()) / len(subjects)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(subjects):
    for marks in subjects.values():
        if marks < 40:
            return "FAIL"
    return "PASS"


def find_highest_subject(subjects):
    return max(subjects, key=subjects.get)


def find_lowest_subject(subjects):
    return min(subjects, key=subjects.get)