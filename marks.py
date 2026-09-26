def get_subject_marks():
    subjects = {}

    number_of_subjects = int(input("Enter number of subjects: "))

    for i in range(number_of_subjects):
        subject = input(f"Enter subject {i + 1} name: ")
        marks = float(input(f"Enter marks in {subject}: "))

        subjects[subject] = marks

    return subjects