# Student Scores Analysis

This project analyzes students' scores in various subjects over multiple semesters using Python and the pandas library. It performs data cleaning, analysis, and visualization on a dataset containing students' scores, and outputs the results in both printed and graphical form.

## Features

The analysis includes the following tasks:
1. **Identifying failing students**: Lists students who scored less than 50 in any subject.
2. **Calculating average scores per subject**: Computes the average score for each subject per semester.
3. **Top-performing student**: Identifies the student with the highest average score across all semesters and subjects.
4. **Most difficult subject**: Finds the subject with the lowest average score across all semesters (i.e., the subject where students struggled the most).
5. **Generating Excel output**: Creates a new Excel file containing average scores per subject for each semester.
6. **Bonus**: Identifies students who consistently improved their scores over the semesters.
7. **Visualizations**: 
   - A bar chart that displays the average score for each subject across all semesters.
   - A line graph showing the overall average score for each semester.

## Installation

To run this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/student-scores-analysis.git
   cd student-scores-analysis
2. Install dependencies: Ensure that you have Python installed (version 3.x). Install the required libraries using pip:
   ```bash
   pip install pandas matplotlib openpyxl
3.Place your dataset: Ensure that your student_scores_random_names.csv file is in the project directory.

## Running The Project
1. Run the python script:
   ```bash
   python main.py
2. The script will output:
      The list of students who failed in any subject.
      The average scores for each subject per semester.
      The top-performing student based on the average score.
      The most difficult subject for students.
      It will also generate an Excel file average_scores_per_semester.xlsx in the project directory.
3. Bonus Output: The script identifies students who have consistently improved their scores across semesters.
4. Visualizations:
     A bar chart showing average scores per subject.
     A line chart showing the overall average score for each semester.
