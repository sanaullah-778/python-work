def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

print("Welcome to Student Result System")

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

grade = calculate_grade(marks)

print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
