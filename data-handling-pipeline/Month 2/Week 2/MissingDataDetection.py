# 1️⃣ Concept
#
# isnull() checks whether each value in the dataset is missing or not.
#
# It returns a Boolean table:
# True → value is missing
# False → value is present


# 2️⃣ Why this exists
#
# In machine learning pipelines, the first step is always data inspection.
#
# We must answer:
# Which columns have missing values?
# Which rows are incomplete?
# How bad is the dataset?
# Before we drop or fill, we must detect.
#
# That detection starts with:
#     df.isnull()


# 3️⃣ Syntax
# df.isnull()
#
# Equivalent function:
# df.isna()
# Both are identical.


import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [25, None, 30, None],
    "Salary": [40000, 50000, None, 60000]
}

df = pd.DataFrame(data)
print(df)
#   Output without .isnull()
#
# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | 40000  |
# | B    | NaN | 50000  |
# | C    | 30  | NaN    |
# | D    | NaN | 60000  |

# 5️⃣ Applying isnull()
# df.isnull()
#
# Output
# Name	Age	Salary
# False	False	False
# False	True	False
# False	False	True
# False	True	False
#
# Interpretation
# True  → missing value
# False → value exists



# 6️⃣ What Pandas Treats as Missing
#
# Pandas considers these as missing:
# NaN
# None
# NaT (for datetime)

import numpy as np

df = pd.DataFrame({
    "A": [1, 2, np.nan],
    "B": [None, 5, 6]
})
df.isnull()


# 7️⃣ Important Detail
#
# isnull() does not count missing values.
# It only detects them.
#
# To count them we later use:
# df.isnull().sum()



# 9️⃣ Visual Intuition
# Think of isnull() as creating a missing-value map.

# Original data
# 25   40000
# NaN  50000
# 30   NaN

# After isnull()
# False False
# True  False
# False True


# 10️⃣ Typical Workflow
#
# Step 1
# df.isnull()
#
# Step 2
# df.isnull().sum()
#
# Step 3
# df.dropna() or df.fillna()

# | Function      | Purpose               |
# | ------------- | --------------------- |
# | `df.isnull()` | Detect missing values |
# | `df.isna()`   | Same as isnull        |
# | Output        | Boolean dataframe     |



# Question 1

# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | 40000  |
# | B    | NaN | 50000  |
# | C    | 30  | NaN    |
# | D    | 28  | 60000  |

d1 = {
    'Name' : ['A' , 'B' , 'C' , 'D'],
    'Age' : [25 , None , 30 ,28],
    'Salary': [40000 , 50000 , None , 60000]
}
df = pd.DataFrame(d1)
print(df[df.isna().any(axis=1)])


# Question 2

import numpy as np

df = pd.DataFrame({
    "A":[1,2,np.nan],
    "B":[None,5,6],
    "C":[7,8,9]
})

print(df.isnull())



### Topic 1.1 (Part 2) — df.isnull().sum()

# 1️⃣ Concept
# df.isnull().sum() counts missing values in each column.

# It answers:
# Which columns contain missing values?
# How many missing values does each column have?

# 2️⃣ Why This Is Important
#
# Imagine a dataset with 100,000 rows and 40 columns.
# You cannot manually inspect it.
# Instead you run:
# df.isnull().sum()

# Example result
# Age        200
# Salary     50
# City        0
# Gender      0


# 3️⃣ How It Works Internally
#
# Step 1
# df.isnull()
#
# Creates a True/False mask.
#
# Example dataset:
# Name	Age	Salary
# A	25	40000
# B	NaN	50000
# C	30	NaN
# D	NaN	60000
#
# df.isnull() →
#
# Name	Age	Salary
# False	False	False
# False	True	False
# False	False	True
# False	True	False
#
# Step 2
#
# .sum()
# Counts True values.
#
# Remember:
# True = 1
# False = 0
#
# Column totals:
# Column	Missing
# Name	0
# Age	2
# Salary	1
#
# Output:
# Name      0
# Age       2
# Salary    1


# 4️⃣ Example Code
# import pandas as pd
#
data = {
    "Name": ["A","B","C","D"],
    "Age": [25,None,30,None],
    "Salary": [40000,50000,None,60000]
}

df = pd.DataFrame(data)
print(df.isnull().sum())  # Similarly for row print(df.isnull().sum(axis=1))
#
# Output:
# Name      0
# Age       2
# Salary    1

# 5️⃣ Real ML Workflow
#
# When you open a dataset:
#
# Step 1 — inspect dataset
# df.head()

# Step 2 — detect missing values
# df.isnull().sum()

# Step 3 — decide strategy
# if missing < 5% → fill
# if missing > 50% → drop column

# 6️⃣ Pro Trick (Very Useful)
#
# Sort columns by missing values:
# df.isnull().sum().sort_values(ascending=False)
#
# Example output:
# Age        200
# Salary      50
# City        10
# Name         0
#
# This instantly shows worst columns first.


# 7️⃣ Another Useful Version
#
# Percentage of missing values:
#
# (df.isnull().sum() / len(df)) * 100
#
# Example:
# Age        20%
# Salary      5%
# City        1%
#
# This is extremely common in ML preprocessing.

# 8️⃣ Important Detail
#
# sum() works column-wise by default.
#
# Meaning:
# axis = 0
# So it counts missing values per column.

## Quick Summary
# | Command                           | Meaning                  |
# | --------------------------------- | ------------------------ |
# | `df.isnull()`                     | Detect missing values    |
# | `df.isnull().sum()`               | Count missing per column |
# | `df.isnull().sum().sort_values()` | Sort by missing          |
# | `(df.isnull().sum()/len(df))*100` | Missing percentage       |


# Questions

# q1
df = pd.DataFrame({
    'Name':['A' , 'B' , 'C' , 'D'],
    'Age' : [25 , None , 30 , None],
    'Salary' : [40000 , 50000 , None , 60000]
})

print(df.isnull().sum())

#q2
# Write code to display only columns that contain missing values.
df = pd.DataFrame({
    'A':[1 , 2 , None],
    'B' : [None , 4 , 7],
    'C' : [5 , 6 , 8]
})
print(df.loc[:, df.isnull().any()])


#q3
# Print the percentage of missing values per column.
df = pd.DataFrame({
    'A':[1 ,None,3],
    'B' : [None , 4 , 6],
    'C' : [3 , None , 7]
})

res = (df.isnull().sum() / len(df)) * 100
print(res)

#q4
# Print columns sorted by number of missing values (highest first).
df = pd.DataFrame({
    'A':[1 , 2 , None],
    'B' : [None , 4 , 7],
    'C' : [5 , 6 , 8]
})

print(df.isnull().sum().sort_values(ascending=False))


#q7
# Return only columns where missing values > 1

df = pd.DataFrame({
    'A':[1 , None , 2 , None],
    'B' : [None , None ,None ,  7],
    'C' : [5 , 6 ,7, 8]
})
missing_count = df.isnull().sum()
print(missing_count[missing_count > 1])

#q8
# Write code to find the column with the maximum missing values.

df = pd.DataFrame({
    'A':[1 , None , 3 , None],
    'B' : [None , None ,None ,  7],
    'C' : [5 , 6 ,7, 8],
    'D' : [7 , 8 , None , 10]
})
# Below is good code but not optimal so optimal is print(df.isnull().sum().idxmax())
missing_count = df.isnull().sum()
max_value = missing_count.max()
print(missing_count[missing_count == max_value])

#q9
# Write code to check if dataset has any missing values at all.

df = pd.DataFrame({
    'A':[1,4,7],
    'B' : [2,None,8],
    'C' : [3,6,9]
})

print(df.isnull().values.any())    # Or print(df.isnull().sum().sum() > 0)

#q10
# Write code to print total missing values in dataset using isnull().sum() logic only.
df = pd.DataFrame({
    'A':[1,None,5],
    'B' : [None,4,6],
    'C' : [3,None,9]
})

m = df.isnull().sum().sum()  # Here the  df.isnull().sum() returns an Series
print(m)






### Topic 1.1 (Part 3) — df.isna().any(axis=1)

# 1️⃣ Concept
# df.isna().any(axis=1)
#
# Returns a Boolean Series for each row:
# True → row contains at least one missing value
# False → row has no missing values

# 2️⃣ Example Dataset
# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | 40000  |
# | B    | NaN | 50000  |
# | C    | 30  | NaN    |
# | D    | 28  | 60000  |

# Step 1 — Detect missing cells

# df.isna()
# | Name  | Age   | Salary |
# | ----- | ----- | ------ |
# | False | False | False  |
# | False | True  | False  |
# | False | False | True   |
# | False | False | False  |

# Step 2 — Check if any column in each row has missing values

# df.isna().any(axis=1)
# Output
# 0    False
# 1    True
# 2    True
# 3    False

# 3️⃣ Why axis=1?
#
# Axis defines direction of operation.
# | Axis     | Meaning             |
# | -------- | ------------------- |
# | `axis=0` | operate column-wise |
# | `axis=1` | operate row-wise    |

# any(axis=1)   # check across columns in each row


# 4️⃣ Most Common Use
#
# Select rows containing missing values.

# df[df.isna().any(axis=1)]
# | Name | Age | Salary |
# | ---- | --- | ------ |
# | B    | NaN | 50000  |
# | C    | 30  | NaN    |


# 5️⃣ Opposite Operation

# Rows without missing values

# df[~df.isna().any(axis=1)]
# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | 40000  |
# | D    | 28  | 60000  |



## Question

#q1
# Print rows that contain missing values.

df = pd.DataFrame({
    "A":[1,2,3],
    "B":[4,5,None],
    "C":[7,8,9]
})

print(df[df.isna().any(axis=1)])


#q2
# Print rows that do NOT contain missing values.

df = pd.DataFrame({
    "A":[1,None,3,4],
    "B":[5,6,None,8],
    "C":[9,10,11,12]
})
print(df[~df.isna().any(axis=1)])


#q3
# Count how many rows contain missing values.

df = pd.DataFrame({
    "A":[1,None,3,4],
    "B":[5,6,None,8],
    "C":[9,10,11,12]
})

print((df.isna().any(axis=1)).sum())  # Here the .sum() does math like if false then adds 0 and if true then adds 1
# print((df.isna().any(axis=1)).count()) here using count gives wrng ans as .count() counts every row that has non NaN value as our each cell has True/False


#q4
# Return indices of rows that contain missing values.

df = pd.DataFrame({
    "A":[1,None,3,None],
    "B":[5,6,7,8],
    "C":[9,None,11,12]
})

t =  df[df.isna().any(axis=1)].index   ## Dataframe as an attribute index so cant call it has an function .index()
# s = df.index[df.isna().any(axis=1)]
print(t)

#q5
# you havnt taught drop or we havent covered till now

##q6
# Check if any row contains missing values.

df = pd.DataFrame({
    "A":[1,2,3],
    "B":[4,5,None],
    "C":[7,8,9]
})

# Error in this as
print(df.isna().values.any(axis = 1))
#
# What .values.any() Does
# Step 1
# df.isnull()
# Creates a boolean DataFrame:
# A	B	C
# False	False	False
# False	False	False
# False	True	False
#
# Step 2
# .values
# Converts the DataFrame into a NumPy array.
#
# Example:
# [[False False False]
#  [False False False]
# [False True False]]
#
# Step 3
# .any()
# Checks if any value is True.
#
# Result:
# True

# Correct answer
r = df.isna().any().any()  #df.isna()        → boolean table
                            #.any()           → column-wise check
                           # .any() again     → overall check
print(r)






### Topic 1.1 (Part 4) — df.isnull().sum().sum()

# 1️⃣ Concept
# df.isnull().sum().sum()
#
# This returns one number.
# That number represents:
# Total missing cells in the dataset


# 2️⃣ How It Works
#
# It happens in 3 steps.
#
# Step 1
#
# df.isnull()
# Creates a True / False mask.

# DataSet
# | A   | B   | C |
# | --- | --- | - |
# | 1   | NaN | 5 |
# | NaN | 4   | 6 |
# | 3   | NaN | 7 |

# Result of .isnull()
# | A     | B     | C     |
# | ----- | ----- | ----- |
# | False | True  | False |
# | True  | False | False |
# | False | True  | False |

# Step 2

df.isnull().sum()
# A    1
# B    2
# C    0

# Step 3

df.isnull().sum().sum()
# Adds all missing counts together.
# 1 + 2 + 0 = 3 # Output


# 3️⃣ Real ML Workflow
#
# When opening a dataset:
#
# df.isnull().sum().sum()
#
# If output is:
# 0
# Dataset is clean.
#
# If output is:
# > 0
# Dataset needs cleaning.


# 4️⃣ Alternative Way
#
# Another way:
# df.isna().values.sum()
#
# But the standard pandas way is:
# df.isnull().sum().sum()


# 5️⃣ Useful Check
#
# Quick check if dataset has missing values:
# df.isnull().sum().sum() > 0
#
# Output:
# True


## Question

#q1
# Print the total number of missing values.

df = pd.DataFrame({
    "A":[1,None,3],
    "B":[4,5,None],
    "C":[7,8,9]
})

print(df.isnull().sum().sum())

#q2
# Check if dataset contains any missing values using this method.

df = pd.DataFrame({
    "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,None]
})

print(df.isnull().values.any())  # or df.isnull().sum().sum() > 0

##q3
# Write code to print: Dataset has X missing values

df = pd.DataFrame({
    "A":[1,None,3,None],
    "B":[4,5,None,7],
    "C":[8,9,10,11]
})

print(f"Dataset has {df.isnull().sum().sum()} missing values")


#q4
# Calculate the percentage of missing values in the entire dataset.

df = pd.DataFrame({
    "A":[1,None,3],
    "B":[4,None,6],
    "C":[None,8,9]
})

missing_percentage = (df.isnull().sum().sum() / df.size) * 100
print(missing_percentage)


#q5
# Write code to print: Dataset is clean or Dataset contains missing values

df = pd.DataFrame({
    "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,None,9]
})

if df.isnull().sum().sum() == 0:
    print("Dataset is clean")
else:
    print("Dataset contains missing values")





