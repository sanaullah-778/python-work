print("Welcome to Student Result System")

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"

print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
