def get_grade(marks):
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


def read_marks(name):
    while True:
        try:
            marks = float(input(f"Enter marks for {name}: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        if not 0 <= marks <= 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            continue

        return marks


students = []

for i in range(1, 6):
    while True:
        name = input(f"Enter name of student {i}: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    marks = read_marks(name)
    grade = get_grade(marks)
    students.append((name, marks, grade))

print("\nStudent Marks Report")
print("-" * 40)
print(f"{'Name':<12} {'Marks':>8} {'Grade':>8}")
print("-" * 40)

for name, marks, grade in students:
    print(f"{name:<12} {marks:>8.1f} {grade:>8}")
