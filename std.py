def get_grade(marks):
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
        raise ValueError('Marks must be between 0 and 100.')


def read_valid_marks(student_name):
    """Read and validate marks from the user."""
    while True:
        try:
            marks = float(input(f"Enter marks for {student_name} (0-100): "))
        except ValueError:
            print("Invalid input: please enter a numeric value.")
            continue

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            continue

        return marks


def main():
    students = []

    for i in range(1, 6):
        while True:
            name = input(f"Enter name of student {i}: ").strip()
            if name:
                break
            print("Name cannot be empty. Please enter a valid name.")

        marks = read_valid_marks(name)
        grade = get_grade(marks)
        students.append((name, marks, grade))

    print("\nStudent Result Summary")
    print("-" * 40)
    print(f"{'Name':<15} {'Marks':>6} {'Grade':>6}")
    print("-" * 40)
    for name, marks, grade in students:
        print(f"{name:<15} {marks:>6.1f} {grade:>6}")


if __name__ == "__main__":
    main()
