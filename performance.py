def calculate_percentage(marks):
    if not marks:
        return 0

    return sum(marks) / len(marks)


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


def calculate_result(marks):
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    return percentage, grade