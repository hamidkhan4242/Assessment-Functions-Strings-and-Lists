# Class Marks Analyzer
# Analyzes marks for a class using lists, loops, and custom functions.

# Gets and validates one student's marks.
def get_valid_mark(student_name):
    while True:
        value = input(f"Enter marks for {student_name} (0-100): ").strip()

        if value.isdigit():
            mark = int(value)
            if 0 <= mark <= 100:
                return mark

        print("Invalid marks. Enter a whole number from 0 to 100.")


# Calculates and returns the class average.
def calculate_average(student_marks):
    return sum(student_marks) / len(student_marks)


# Displays every student who achieved the highest and lowest marks.
def display_extreme_students(student_names, student_marks):
    highest_marks = max(student_marks)
    lowest_marks = min(student_marks)

    print("\n===== HIGHEST MARKS =====")
    print(f"Highest marks: {highest_marks}")
    for index in range(len(student_marks)):
        if student_marks[index] == highest_marks:
            print(student_names[index])

    print("\n===== LOWEST MARKS =====")
    print(f"Lowest marks: {lowest_marks}")
    for index in range(len(student_marks)):
        if student_marks[index] == lowest_marks:
            print(student_names[index])


# Counts and returns the number of passing and failing students.
def count_pass_fail(student_marks):
    passing = 0
    failing = 0

    for mark in student_marks:
        if mark >= 50:
            passing += 1
        else:
            failing += 1

    return passing, failing


# Displays all students whose marks are above the class average.
def display_above_average(student_names, student_marks, average):
    print("\n===== ABOVE CLASS AVERAGE =====")
    found_student = False

    for index in range(len(student_marks)):
        if student_marks[index] > average:
            print(f"{student_names[index]}: {student_marks[index]}")
            found_student = True

    if not found_student:
        print("No students scored above the class average.")


# Main program
print("========== CLASS MARKS ANALYZER ==========")

# Get a valid positive number of students.
while True:
    number_text = input("Enter number of students: ").strip()

    if number_text.isdigit() and int(number_text) > 0:
        number_of_students = int(number_text)
        break

    print("Invalid input. Enter a positive whole number.")

# Create the two required lists.
student_names = []
student_marks = []

# Collect each student's name and mark.
for student_number in range(number_of_students):
    print(f"\nStudent {student_number + 1}")

    while True:
        name = input("Enter student name: ").strip().title()
        if name:
            break
        print("Name cannot be empty. Please try again.")

    mark = get_valid_mark(name)

    # Append the student's information to the separate lists.
    student_names.append(name)
    student_marks.append(mark)

# Calculate class statistics.
class_average = calculate_average(student_marks)
passing_students, failing_students = count_pass_fail(student_marks)

# Display the class analysis report.
print("\n" + "=" * 46)
print("             CLASS ANALYSIS REPORT")
print("=" * 46)
print(f"Total students : {len(student_names)}")
print(f"Class average  : {class_average:.2f}")

display_extreme_students(student_names, student_marks)

print("\n===== PASSING AND FAILING =====")
print(f"Passing students: {passing_students}")
print(f"Failing students: {failing_students}")

display_above_average(student_names, student_marks, class_average)

# Sort a copy of the marks from highest to lowest.
sorted_marks = sorted(student_marks, reverse=True)
print("\n===== MARKS: HIGHEST TO LOWEST =====")
print(sorted_marks)

print("=" * 46)
print("           ANALYSIS COMPLETED")
print("=" * 46)
