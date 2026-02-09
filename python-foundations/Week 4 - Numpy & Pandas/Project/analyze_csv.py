import pandas as pd
import numpy as np


def grade_cal(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    else:
        return "F"


# Load CSV data
data = pd.read_csv(
    "students.csv",
    sep=",",
    dtype={"Score": "int"}
)

print(f"Loaded: {data.shape[0]} students")

# Convert Score column to NumPy array
scores = data["Score"].values

# NumPy statistics
avg_score = np.mean(scores)
max_score = np.max(scores)
spread_of_scores = np.std(scores)

print(f"NumPy Mean: {avg_score:.1f}")
print(f"NumPy Max: {max_score}")
print(f"NumPy Std: {spread_of_scores:.1f}")

# Vectorized comparison and filtering
no_of_student_qualify = (data["Score"] > 80).sum()
print(f"Top performers (>80): {no_of_student_qualify}")

# Adding new columns
data["Grade"] = data["Score"].apply(grade_cal)
data["Pass"] = data["Score"] >= 75

# Export processed data
data.to_csv(
    path_or_buf="students_graded.csv",
    encoding="utf-8",
    index=False
)

print("✅ Saved: students_graded.csv")
