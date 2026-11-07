# Student Result Card Generator
# Generates a result card for one student using functions and string methods.

# Gets and validates marks for one subject.
def get_valid_marks(subject):
    while True:
        value = input(f"Enter marks for {subject} (0-100): ").strip()

        if value.isdigit():
            marks = int(value)
            if 0 <= marks <= 100:
                return marks

        print("Invalid marks. Enter a whole number from 0 to 100.")


# Calculates the percentage from obtained and maximum marks.
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


# Returns the grade for the supplied percentage.
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# Removes extra spaces and formats the student's name in title case.
def format_name(name):
    return name.strip().title()


# Main program
print("===== STUDENT RESULT CARD GENERATOR =====")

# Get and format the student's name.
while True:
    student_name = format_name(input("Enter student name: "))
    if student_name:
        break
    print("Name cannot be empty. Please try again.")

# Get a roll number containing digits only.
while True:
    roll_number = input("Enter roll number: ").strip()
    if roll_number.isdigit():
        break
    print("Invalid roll number. Use digits only.")

# Collect marks for five subjects.
subjects = ["English", "Mathematics", "Computer", "Physics", "Chemistry"]
student_marks = []

for subject in subjects:
    student_marks.append(get_valid_marks(subject))

# Calculate total, percentage, and grade.
total_obtained = sum(student_marks)
maximum_total = len(subjects) * 100
percentage = calculate_percentage(total_obtained, maximum_total)
grade = get_grade(percentage)

# A student fails if any subject mark is below 40.
if any(mark < 40 for mark in student_marks):
    final_status = "Fail"
else:
    final_status = "Pass"

# Display the formatted result card.
print("\n" + "=" * 42)
print("             STUDENT RESULT CARD")
print("=" * 42)
print(f"Student Name    : {student_name}")
print(f"Roll Number     : {roll_number}")
print("-" * 42)
print(f"{'Subject':<22}{'Marks':>10}")
print("-" * 42)

for subject, marks in zip(subjects, student_marks):
    print(f"{subject:<22}{marks:>10}")

print("-" * 42)
print(f"Total Marks     : {total_obtained} / {maximum_total}")
print(f"Percentage      : {percentage:.2f}%")
print(f"Grade           : {grade}")
print(f"Final Status    : {final_status}")
print("=" * 42)
