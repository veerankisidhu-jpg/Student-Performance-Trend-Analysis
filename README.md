# Student-Performance-Trend-Analysis 
 Student Performance Trend Analysis
1. Project Description
This Python project analyzes student marks across multiple examinations. It compares assessment scores, calculates improvements and declines, identifies consistently weak subjects, and classifies students using defined criteria.
2. Features
- Exam-wise average score calculation
- Comparison of the first and last examination
- Subject-wise score trends
- Identification of consistently weak subjects
- Overall student average and classification
- Class performance summary
3. Technologies Used
- Python 3
- Python built-in functions and data structures
- No external libraries required
4. Project Files
- student_performance.py - Complete Python source code
- README.md - Project documentation
5. Data Format
Each student record contains:
- Student name
- A nested list of scores for each examination
- Scores are arranged in the same order as the SUBJECTS list
Example:
["Ananya", [[78, 65, 72, 80], [84, 70, 76, 82], [90, 75, 80, 85]]]
The inner lists represent Exam 1, Exam 2, and Exam 3 respectively.
6. Classification Criteria
Overall Average	Classification
85 and above	Excellent
70 to below 85	Good
50 to below 70	Average
Below 50	Needs Improvement


7. Weak Subject Criteria
A subject is identified as consistently weak when the student's score is below 50 in at least 2 examinations.
8. How to Run
1. Install Python 3.
2. Save student_performance.py.
3. Open a terminal or command prompt in the project folder.
4. Run:
python student_performance.py
On some systems, use:
python3 student_performance.py
9. How to Customize
- Add or remove subjects in the SUBJECTS list.
- Add examination names in EXAM_NAMES.
- Add student records to the students list.
- Update PASS_MARK, WEAK_SUBJECT_LIMIT, or WEAK_EXAM_COUNT to change analysis rules.
- Ensure each exam contains the same number of subject scores as the SUBJECTS list.
10. Concepts Demonstrated
Variables, data types, lists, nested lists, functions, loops, conditional statements, arithmetic operations, formatted output, and problem-solving logic.
