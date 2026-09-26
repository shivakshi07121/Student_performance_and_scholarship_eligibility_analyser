def check_scholarship(percentage, attendance, family_income):

    # Normal eligibility condition
    normal_condition = (
        percentage >= 75
        and attendance >= 80
        and family_income < 500000
    )

    # Special condition for students scoring above 90%
    special_condition = (
        percentage > 90
        and 70 <= attendance <= 80
        and family_income < 500000
    )

    if normal_condition:
        return "ELIGIBLE", "All normal scholarship conditions are satisfied."

    elif special_condition:
        return "ELIGIBLE", "Eligible under the special high-percentage condition."

    else:
        return "NOT ELIGIBLE", "Scholarship conditions are not satisfied."