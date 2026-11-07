# Python Functions and Lists Assessment

## Project Overview

This repository contains two separate beginner-level Python programs. They demonstrate functions, string manipulation, lists, loops, conditional statements, built-in functions, and input validation.

## Programs

### 1. Student Result Card Generator

**File:** `result_card_generator.py`

This program asks for one student's name, roll number, and marks in five subjects. It validates the inputs, calculates total marks and percentage, assigns a grade, and displays a formatted result card.

A student receives a final status of **Fail** if any subject mark is below 40, regardless of the overall percentage.

### 2. Class Marks Analyzer

**File:** `class_marks_analyzer.py`

This program collects the names and marks of all students in a class. It calculates the class average, identifies all students with the highest and lowest marks, counts passing and failing students, displays students above the class average, and sorts marks from highest to lowest.

A mark of 50 or above is counted as a pass.

## Python Concepts and Functions Used

- **Custom functions:** `def`, parameters, and `return`
- **String methods:** `.strip()`, `.title()`, and `.isdigit()`
- **Lists:** list creation, `.append()`, indexing, and iteration
- **Built-in functions:** `len()`, `sum()`, `max()`, `min()`, `sorted()`, and `any()`
- **Loops:** `for` and `while`
- **Conditions:** `if`, `elif`, and `else`
- **Formatted output:** f-strings
- **Input validation:** checking values and asking again when input is invalid

## Requirements

- Python 3
- A terminal or Python editor such as IDLE or Visual Studio Code

No third-party Python packages are required.

## How to Run

Open a terminal in the project folder.

Run the Student Result Card Generator:

```bash
python result_card_generator.py
```

Run the Class Marks Analyzer:

```bash
python class_marks_analyzer.py
```

On some systems, use `python3` instead of `python`.

## Sample Input and Output

### Student Result Card Generator

Sample input:

```text
Student name: Hamid Ahmad Khan
Roll number: 50
English: 85
Mathematics: 90
Computer: 95
Physics: 80
Chemistry: 75
```

Sample result:

```text
Student Name    : Hamid Ahmad Khan
Roll Number     : 50
Total Marks     : 425 / 500
Percentage      : 85.00%
Grade           : A
Final Status    : Pass
```

### Class Marks Analyzer

Sample input:

```text
Number of students: 4
Hamid: 85
Ayesha: 90
Ali: 45
Sara: 70
```

Sample result:

```text
Total students : 4
Class average  : 72.50
Highest marks  : 90 (Ayesha)
Lowest marks   : 45 (Ali)
Passing students: 3
Failing students: 1
Above average:
Hamid: 85
Ayesha: 90
Marks highest to lowest: [90, 85, 70, 45]
```

## Testing

Test each program with multiple scenarios, including:

- Valid inputs.
- Non-numeric marks and out-of-range marks.
- Boundary marks such as 0, 40, 50, and 100.
- Multiple students tied for the highest or lowest mark.
- A student who scores below 40 in one subject in the result card program.

## Repository Structure

```text
python-functions-lists-assessment/
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```
