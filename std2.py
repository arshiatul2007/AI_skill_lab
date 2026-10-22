def calculate_average(marks):
    """
    Calculate the arithmetic mean of a list of marks.
    Requirements:
    - reject empty list
    - reject any mark outside 0-100
    - preserve the original list
    - return the arithmetic mean
    """
    # Reject empty list.
    if not marks:
        raise ValueError("Marks list cannot be empty.")

    # Make a copy so the original list is never changed.
    copied_marks = list(marks)

    # Check every mark individually.
    for mark in copied_marks:
        # Reject non-numeric values as invalid input.
        if not isinstance(mark, (int, float)):
            raise TypeError("Each mark must be a number.")
        # Reject marks outside the allowed range.
        if mark < 0 or mark > 100:
            raise ValueError("Each mark must be between 0 and 100.")

    # Calculate arithmetic mean.
    total = sum(copied_marks)
    average = total / len(copied_marks)
    return average


def calculate_grade(marks):
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


def get_valid_mark(student_name):
    while True:
        try:
            marks = float(input(f"Enter marks for {student_name}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid mark! Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


# -------------------------------
# Normal test cases
# -------------------------------
print(calculate_average([50, 60, 70, 80, 90]))
print(calculate_average([10, 20, 30]))

# -------------------------------
# Boundary test cases
# -------------------------------
print(calculate_average([0, 50, 100]))
print(calculate_average([100, 100, 100]))

# -------------------------------
# Invalid input tests
# -------------------------------
try:
    print(calculate_average([]))
except Exception as e:
    print(type(e).__name__, e)

try:
    print(calculate_average([10, 20, 101]))
except Exception as e:
    print(type(e).__name__, e)

try:
    print(calculate_average([10, 'x', 30]))
except Exception as e:
    print(type(e).__name__, e)

# Demonstrate that the original list is preserved.
original = [20, 30, 40]
copy_before = list(original)
result = calculate_average(original)
print("Original list after call:", original)
print("Expected same as before:", original == copy_before)
print("Average:", result)


# -------------------------------
# Student result summary
# -------------------------------
students = []

for i in range(1, 6):
    name = input(f"Enter name of student {i}: ").strip()
    marks = get_valid_mark(name)
    grade = calculate_grade(marks)
    students.append((name, marks, grade))

print("\nStudent Result Summary")
print("-" * 45)
print(f"{'Name':<12} {'Marks':>8} {'Grade':>8}")
print("-" * 45)

for name, marks, grade in students:
    print(f"{name:<12} {marks:>8.1f} {grade:>8}")

print("-" * 45)
