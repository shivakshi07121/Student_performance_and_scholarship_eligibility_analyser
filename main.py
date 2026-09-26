from student import get_student_details
from marks import get_subject_marks

from performance import (
    calculate_total,
    calculate_percentage,
    calculate_average,
    calculate_grade,
    check_pass_fail,
    find_highest_subject,
    find_lowest_subject
)

from scholarship import check_scholarship

from validation import validate_attendance, validate_income

from report import generate_report


# ==========================================
# STUDENT PERFORMANCE & SCHOLARSHIP ANALYZER
# ==========================================

print("=" * 55)
print("      STUDENT PERFORMANCE & SCHOLARSHIP ANALYZER")
print("=" * 55)


# ------------------------------------------
# 1. Get Student Details
# ------------------------------------------

name, roll_number, branch, semester = get_student_details()


# ------------------------------------------
# 2. Get Subject Marks
# ------------------------------------------

subjects = get_subject_marks()


# ------------------------------------------
# 3. Performance Analysis
# ------------------------------------------

total = calculate_total(subjects)

percentage = calculate_percentage(subjects)

average = calculate_average(subjects)

grade = calculate_grade(percentage)

result = check_pass_fail(subjects)

highest_subject = find_highest_subject(subjects)

lowest_subject = find_lowest_subject(subjects)


# ------------------------------------------
# 4. Get Attendance
# ------------------------------------------

print("\n---------- ATTENDANCE ----------")

while True:
    try:
        attendance = float(
            input("Enter attendance percentage: ")
        )

        valid, message = validate_attendance(attendance)

        if valid:
            break

        print("Error:", message)

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# 5. Get Family Income
# ------------------------------------------

print("\n---------- FAMILY INCOME ----------")

while True:
    try:
        family_income = float(
            input("Enter annual family income: ")
        )

        valid, message = validate_income(family_income)

        if valid:
            break

        print("Error:", message)

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# 6. Check Scholarship Eligibility
# ------------------------------------------

scholarship_status, scholarship_reason = check_scholarship(
    percentage,
    attendance,
    family_income
)


# ------------------------------------------
# 7. Generate Final Report
# ------------------------------------------

generate_report(
    name,
    roll_number,
    branch,
    semester,
    subjects,
    total,
    percentage,
    average,
    grade,
    result,
    highest_subject,
    lowest_subject,
    attendance,
    family_income,
    scholarship_status,
    scholarship_reason
)