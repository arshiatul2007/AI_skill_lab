# Program: Student Marks and Grade Report
# This program accepts marks for 5 students, validates them,
# calculates grades, and displays a formatted report.

# Grade boundaries:
# 90-100 -> A
# 80-89  -> B
# 70-79  -> C
# 60-69  -> D
# 50-59  -> E
# 0-49   -> F


def calculate_grade(marks):
    """Return the grade for a given marks value."""
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks <= 89:
        return 'B'
    elif 70 <= marks <= 79:
        return 'C'
    elif 60 <= marks <= 69:
        return 'D'
    elif 50 <= marks <= 59:
        return 'E'
    elif 0 <= marks <= 49:
        return 'F'
    else:
        raise ValueError("Marks must be between 0 and 100.")


def input_valid_marks(student_name):
    """Keep asking until the user enters a valid numeric mark in the range 0-100."""
    while True:
        try:
            marks = float(input(f"Enter marks for {student_name}: "))
        except ValueError:
            # This handles invalid input like letters or symbols.
            print("Invalid input! Please enter a numeric value.")
            continue

        if marks < 0 or marks > 100:
            # This handles marks outside the valid range.
            print("Invalid marks! Marks must be between 0 and 100.")
            continue

        return marks


# Main program
students = []

for i in range(1, 6):
    while True:
        name = input(f"Enter name of student {i}: ").strip()
        if name:
            break
        print("Name cannot be empty. Please enter a valid name.")

    marks = input_valid_marks(name)
    grade = calculate_grade(marks)
    students.append((name, marks, grade))

# Display a neatly formatted report
print("\nSTUDENT RESULTS REPORT")
print("-" * 45)
print(f"{'Name':<12} {'Marks':>8} {'Grade':>8}")
print("-" * 45)

for name, marks, grade in students:
    print(f"{name:<12} {marks:>8.1f} {grade:>8}")

print("-" * 45)

# ------------------------------------------------------------------
# TEST CASES FOR BOUNDARY VALUES
# ------------------------------------------------------------------
# 1) 89 should be B
# 2) 90 should be A
# 3) 0 should be F
# 4) 100 should be A
# 5) 49 should be F
# 6) 50 should be E
#
# Example:
# marks = 89  -> grade B
# marks = 90  -> grade A
# marks = 49  -> grade F
# marks = 50  -> grade E
# marks = 100 -> grade A
#
# Invalid tests:
# - "abc" -> non-numeric input, ask again
# - -5     -> outside 0-100, ask again
# - 120    -> outside 0-100, ask again
# ------------------------------------------------------------------