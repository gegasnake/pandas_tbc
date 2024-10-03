import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('student_scores_random_names.csv')

# 1. Here I find students who failed
failed_students = df[df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].lt(50).any(axis=1)]['Student'].unique()
print("Students who failed at least one subject:\n", failed_students)

# 2. Here I calculate average score per subject in each semester
average_scores_per_semester = df.groupby('Semester').mean(numeric_only=True)
print("\nAverage scores per subject in each semester:\n", average_scores_per_semester)

# 3. Here I find student(s) with the highest average score across all semesters and subjects
df['Average_Score'] = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean(axis=1)
highest_avg_students = df.groupby('Student')['Average_Score'].mean().idxmax()
print("\nStudent with the highest average score:", highest_avg_students)

# 4. Here I find the subject where students struggled the most (lowest average score)
subject_difficulty = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean().idxmin()
print("\nSubject with the lowest average score (most difficult):", subject_difficulty)

# 5. Here I generate a new DataFrame with average subject scores per semester and save it as an Excel file
average_scores_df = df.groupby('Semester').mean(numeric_only=True)
output_file_path = 'average_scores_per_semester.xlsx'
average_scores_df.to_excel(output_file_path)
print(f"\nAverage scores per semester saved to {output_file_path}")


# Bonus: Find students who consistently improved their scores
def consistently_improved(data):
    return all(x < y for x, y in zip(data, data[1:]))


students_improved = df.groupby('Student')['Average_Score'].apply(lambda x: consistently_improved(x.dropna().values))
improved_students = students_improved[students_improved].index.tolist()
print("\nStudents who consistently improved their scores:\n", improved_students)


# Bar chart for average subject scores across all semesters
average_subject_scores = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()
average_subject_scores.plot(kind='bar', title="Average Subject Scores")
plt.ylabel('Score')
plt.show()

# Line chart for average overall score per semester
average_overall_score = df.groupby('Semester')['Average_Score'].mean()
average_overall_score.plot(kind='line', marker='o', title="Average Overall Score per Semester")
plt.ylabel('Average Score')
plt.show()
