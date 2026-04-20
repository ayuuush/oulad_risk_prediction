import pandas as pd

# 1. Load the Anchor Table (Courses)
courses_df = pd.read_csv('data/courses.csv')

# 2. Load the Demographic/Outcome Table (Student Info)
student_info_df = pd.read_csv('data/studentInfo.csv')

# 3. Print the verification metrics
print("--- Courses Info ---")
print(courses_df.info())
print("\n--- Student Info ---")
print(student_info_df.info())
print("\n--- Missing Values in Student Info ---")
print(student_info_df.isnull().sum())