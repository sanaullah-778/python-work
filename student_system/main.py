print("Welcome to Student Result System")

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("Student:", name)
print("Marks:", marks)
print("Result:", result)
