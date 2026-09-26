# Student Performance & Scholarship Analyzer

## 1. Project Overview

The Student Performance & Scholarship Analyzer is a Python-based project developed as a first-semester B.Tech CSE project.

The main purpose of this project is to collect student academic information, analyze their performance, and determine whether they are eligible for a scholarship based on predefined eligibility criteria.

The project demonstrates basic problem-solving and programming concepts such as:
- Input and output
- Variables and data types
- Functions
- Lists and dictionaries
- Conditional statements
- Logical operators
- Modular programming
- Input validation
- Data processing
- Formatted output

---

## 2. Problem Statement

Colleges need a simple and systematic way to analyze student performance and identify students who satisfy scholarship eligibility conditions.

The system takes student details, subject marks, attendance percentage, and annual family income as input.

It then calculates:
- Total marks
- Percentage
- Average marks
- Grade
- Pass/Fail status
- Highest-scoring subject
- Lowest-scoring subject
- Scholarship eligibility

---

## 3. Objectives

The objectives of this project are:

1. To collect student information.
2. To collect marks for multiple subjects.
3. To calculate the student's total marks and percentage.
4. To determine the student's average and grade.
5. To determine Pass/Fail status.
6. To identify the highest and lowest scoring subjects.
7. To check scholarship eligibility.
8. To display a clear student performance report.
9. To demonstrate modular programming using multiple Python files.
10. To apply problem-solving concepts to a real-world problem.

---

## 4. Scholarship Eligibility Criteria

The scholarship eligibility is based on the following conditions:

### Normal Eligibility

A student is eligible when:

- Percentage is at least 75%.
- Attendance is at least 80%.
- Annual family income is below ₹50,000.

### Special Eligibility

Students with a percentage above 90% are given special consideration even when their attendance is between 70% and 80%, according to the project problem statement.

The conditions are implemented using logical operators and conditional statements.

---

## 5. Input

The program accepts the following information:

### Student Details
- Student name
- Roll number
- Branch
- Semester

### Academic Details
- Number of subjects
- Subject names
- Marks obtained in each subject

### Additional Information
- Attendance percentage
- Annual family income

---

## 6. Processing

The program performs the following processing:

1. Accepts student details.
2. Accepts subject names and marks.
3. Calculates total marks.
4. Calculates percentage.
5. Calculates average marks.
6. Assigns a grade.
7. Determines Pass/Fail status.
8. Finds the highest-scoring subject.
9. Finds the lowest-scoring subject.
10. Checks scholarship eligibility.
11. Generates the final report.

---

## 7. Output

The program displays a student performance report containing:

- Student name
- Roll number
- Branch
- Semester
- Subject-wise marks
- Total marks
- Percentage
- Average marks
- Grade
- Pass/Fail status
- Highest-scoring subject
- Lowest-scoring subject
- Attendance
- Family income
- Scholarship eligibility

---

## 8. Project Structure

The project is divided into different Python modules.

```text
Student Performance Scholarship Analyzer
│
├── main.py
├── student.py
├── marks.py
├── performance.py
├── scholarship.py
├── validation.py
├── report.py
└── README.md
