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

added_students = set()

while True:
    name = input("\nEnter student name (or type 'exit' to stop): ")

    if name.lower() == "exit":
        break

    if name.lower() in added_students:
        print("⚠️ Name already added")
        continue

    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("❌ Invalid marks. Please enter a number.")
        continue

    grade = calculate_grade(marks)
    added_students.add(name.lower())

    print("\n--- Result ---")
    print("Student:", name)
    print("Marks:", marks)
    print("Grade:", grade)
