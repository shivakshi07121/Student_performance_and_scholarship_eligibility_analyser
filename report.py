def generate_report(
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
):
    print("\n")
    print("=" * 55)
    print("        STUDENT PERFORMANCE REPORT")
    print("=" * 55)

    print("\nSTUDENT DETAILS")
    print("-" * 55)
    print("Name              :", name)
    print("Roll Number       :", roll_number)
    print("Branch            :", branch)
    print("Semester          :", semester)

    print("\nSUBJECT PERFORMANCE")
    print("-" * 55)

    for subject, marks in subjects.items():
        print(f"{subject:<20}: {marks}/100")

    print("\nPERFORMANCE SUMMARY")
    print("-" * 55)
    print("Total Marks       :", total)
    print("Percentage        :", round(percentage, 2), "%")
    print("Average Marks     :", round(average, 2))
    print("Grade             :", grade)
    print("Result            :", result)
    print("Highest Subject   :", highest_subject)
    print("Lowest Subject    :", lowest_subject)

    print("\nSCHOLARSHIP DETAILS")
    print("-" * 55)
    print("Attendance        :", attendance, "%")
    print("Family Income     : ₹", family_income)
    print("Scholarship       :", scholarship_status)
    print("Reason            :", scholarship_reason)

    print("=" * 55)
    print("             END OF REPORT")
    print("=" * 55)