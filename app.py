import json
from performance import calculate_result


FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    # Check duplicate roll number
    for student in students:
        if student["roll_no"] == roll_no:
            print("A student with this roll number already exists.")
            return

    marks = []

    subjects = ["Python", "Java", "DBMS", "Computer Networks"]

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter marks between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    percentage, grade = calculate_result(marks)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    save_students(students)

    print("\nStudent added successfully!")
    print("Percentage:", percentage)
    print("Grade:", grade)


def view_students():
    print("\n--- Student Performance ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])
        print("Percentage:", student["percentage"])
        print("Grade:", student["grade"])


def search_student():
    print("\n--- Search Student ---")

    roll_no = input("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            print("Percentage:", student["percentage"])
            print("Grade:", student["grade"])
            return

    print("Student not found.")


def main():
    while True:

        print("\n====================================")
        print(" Student Performance Tracking System")
        print("====================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("\nThank you!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()