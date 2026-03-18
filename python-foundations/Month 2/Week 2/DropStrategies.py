
### Topic 1.2.1 — df.dropna()

# 1️⃣ Concept
# df.dropna()
# Removes rows that contain any missing value.
#
# Meaning:
# If any column in a row has NaN → that row is removed.

# 2️⃣ Example Dataset
import pandas as pd

df = pd.DataFrame({
    "A":[1,2,None,4],
    "B":[5,None,7,8],
    "C":[9,10,11,12]
})
print(df)

# Output
# | index | A   | B   | C  |
# | ----- | --- | --- | -- |
# | 0     | 1   | 5   | 9  |
# | 1     | 2   | NaN | 10 |
# | 2     | NaN | 7   | 11 |
# | 3     | 4   | 8   | 12 |

print(df.dropna())


# 4️⃣ Why Rows Were Removed
#
# Row 1 removed because:
# B = NaN
# Row 2 removed because:
# A = NaN

# Pandas rule:
# Row contains NaN → drop row

# 5️⃣ Important Detail
# dropna() does NOT modify the original DataFrame.
#
# Example:
# df.dropna()
# print(df)
# The original DataFrame remains unchanged.

# To permanently change it:
# df = df.dropna()
# or
# df.dropna(inplace=True)

# 6️⃣ Default Behavior
#
# dropna() internally means:
# df.dropna(axis=0, how="any")
#
# Meaning:
# axis=0 → operate on rows
# how="any" → drop if ANY NaN appears

#
# 7️⃣ Real ML Example
#
# Imagine a dataset:
#
# Age	Salary	Experience
# 25	40000	2
# NaN	50000	3
# 30	NaN	5
#
# Running:
# df.dropna()
#
# Result:
#
# Age	Salary	Experience
# 25	40000	2
# But this is dangerous sometimes because:
# You might lose too much data.
# That's why we later learn better strategies.


## Question

#q1
# Drop rows containing missing values.
df = pd.DataFrame({
    "A":[1,2,None,4],
    "B":[5,None,7,8],
    "C":[9,10,11,12]
})

print(df.dropna())

#q2
# Store the cleaned DataFrame in a variable called clean_df.
df = pd.DataFrame({
    "A":[1,None,3],
    "B":[4,5,None],
    "C":[7,8,9]
})

clean_df = df.dropna()

#q3
# Drop rows with missing values without modifying the original dataframe.

df = pd.DataFrame({
    "A":[1,None,3,4],
    "B":[5,6,None,8],
    "C":[9,10,11,12]
})

print(df.dropna())






### Topic 1.2.2 — axis in dropna()
#
# 1️⃣ Concept
# df.dropna(axis=...)
# axis decides WHAT you are dropping.

# | axis     | Meaning          |
# | -------- | ---------------- |
# | `axis=0` | drop **rows**    |
# | `axis=1` | drop **columns** |

# 2️⃣ Example Dataset

df = pd.DataFrame({
    "A":[1,2,None,4],
    "B":[5,None,7,8],
    "C":[9,10,11,12]
})
#
# | index | A   | B   | C  |
# | ----- | --- | --- | -- |
# | 0     | 1   | 5   | 9  |
# | 1     | 2   | NaN | 10 |
# | 2     | NaN | 7   | 11 |
# | 3     | 4   | 8   | 12 |

# 3️⃣ Case 1 — axis=0 (Drop Rows)

# df.dropna(axis=0)
# | index | A | B | C  |
# | ----- | - | - | -- |
# | 0     | 1 | 5 | 9  |
# | 3     | 4 | 8 | 12 |

# 4️⃣ Case 2 — axis=1 (Drop Columns)
# | index | C  |
# | ----- | -- |
# | 0     | 9  |
# | 1     | 10 |
# | 2     | 11 |
# | 3     | 12 |

# 5️⃣ Key Insight
# axis=0 → check row-wise
# “Does this row contain NaN?”

# axis=1 → check column-wise
# “Does this column contain NaN?”

# 6️⃣ Real ML Insight

# ⚠ Important:
# axis=1 is very dangerous
# Why?
# Because:
# You might delete entire important features (columns)
#
# Example:
# If "Salary" column has 5 missing values → it gets removed completely
#
# So usually:
# We prefer axis=0 (drop rows)



## Questions

# q1 Drop rows containing missing values using axis.
df = pd.DataFrame({
    "A":[1,None,3],
    "B":[4,5,None],
    "C":[7,8,9]
})

print(df.dropna(axis=0))

# q2 Drop columns containing missing values.
df = pd.DataFrame({
    "A":[1,None,3],
    "B":[4,5,6],
    "C":[7,None,9]
})

dffinal = df.dropna(axis = 1)
print(dffinal)


## q4
# Print:
# Rows before: X
# Rows after dropping rows: Y
# Columns after dropping columns: Z

df = pd.DataFrame({
    "A":[1,None,3,None],
    "B":[5,6,7,8],
    "C":[9,None,11,12]
})

print("Rows Before: ")
print(df)

print("Rows after dropping rows: ")
print(df.dropna(axis=0))

print("Columns after dropping columns: ")
print(df.dropna(axis = 1))


## q5
# Check if any column is completely removed after axis=1.
df = pd.DataFrame({
    "A":[1,2,3],
    "B":[4,None,6],
    "C":[7,8,9]
})

print(f"Before columns operation: {df.shape[1]}") # OR can use len(df.columns) to calulate the total columns
df = df.dropna(axis=1)
print(f"After columns operation: {df.shape[1]}") # OR can use len(df.columns) to calulate the total columns




### Topic 1.2.3 — how="any" vs how="all" in dropna()

# 1️⃣ Concept
# df.dropna(how="any")
# df.dropna(how="all")
# Parameter	Meaning
# how="any"	drop if ANY value is NaN
# how="all"	drop only if ALL values are NaN

# 2️⃣ Example Dataset
# df = pd.DataFrame({
#     "A":[1,None,None],
#     "B":[5,None,None],
#     "C":[9,10,None]
# })
# index	A	B	C
# 0	1	5	9
# 1	NaN	NaN	10
# 2	NaN	NaN	NaN

# 3️⃣ Case 1 — how="any"
# df.dropna(how="any")
# Rule
# Drop row if it contains even ONE NaN
# Output:
# index	A	B	C
# 0	1	5	9
#
# Explanation:
# Row 1 → has NaN → removed
# Row 2 → has NaN → removed

# 4️⃣ Case 2 — how="all"
# df.dropna(how="all")
# Rule
# Drop row only if ALL values are NaN
# Output:
# index	A	B	C
# 0	1	5	9
# 1	NaN	NaN	10
#
# Explanation:
# Row 2 → all NaN → removed
# Row 1 → has some values → kept

# 5️⃣ With Columns (axis=1)
# df.dropna(axis=1, how="any")
#
# Drop columns with any missing values
# df.dropna(axis=1, how="all")
# Drop columns only if entire column is NaN

# 6️⃣ Key Difference (Very Important)
# Case	Behavior
# any	aggressive → removes more data
# all	safe → removes only useless data

# 7️⃣ Real ML Insight
# When to use how="any"
# When you want clean dataset with no missing values
# When to use how="all"
# When removing useless rows/columns (completely empty)


## Questions

#q1
df = pd.DataFrame({
    "A":[None,None,3],
    "B":[None,None,7],
    "C":[None,None,9]
})

print(df)
df = df.dropna(axis=0 , how="all")
print(df)

#q2
df = pd.DataFrame({
    "A":[1,None,None],
    "B":[5,None,None],
    "C":[9,10,None]
})

print("Rows before operation: ")
print(df)

print("Rows after using how=any")
print(df.dropna(how = "any"))

print("Rows after using how=all")
print(df.dropna(how = "all"))




### Topic 1.2.4 — subset in dropna()

# 1️⃣ Concept
# df.dropna(subset=["column_name"])
#
# This means:
# Drop rows ONLY if specific column(s) contain missing values


# 2️⃣ Why This Is Important
#
# Sometimes:
# Not all columns are equally important

# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | 40000  |
# | B    | NaN | 50000  |
# | C    | 30  | NaN    |
#
# If you run:
# df.dropna()
#
# Output:
# Name	Age	Salary
# A	25	40000


# 3️⃣ Using subset
# df.dropna(subset=["Age"])

# Rule: Drop row only if Age is missing Ignore other columns

# Output
# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | 40000  |
# | C    | 30  | NaN    |

# 4️⃣ Multiple Columns
# df.dropna(subset=["Age", "Salary"])

# Rule: Drop row if ANY of these columns have NaN

# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | 40000  |
# | B    | NaN | 50000  |
# | C    | 30  | NaN    |

# df.dropna(subset=["Age", "Salary"])
# | Name | Age | Salary |
# | ---- | --- | ------ |
# | A    | 25  | 40000  |



# 5️⃣ Key Insight
# | Case                       | Behavior            |
# | -------------------------- | ------------------- |
# | `dropna()`                 | checks ALL columns  |
# | `dropna(subset=["Age"])`   | checks only Age     |
# | `dropna(subset=["A","B"])` | checks only A and B |

# 6️⃣ Real ML Use Case
#
# Example:
# Target column = Salary
#
# You MUST remove rows where target is missing:
# df.dropna(subset=["Salary"])
# But you may keep other missing values and fill them later.


## Question

# q1
# Drop rows where column A has missing values.
df = pd.DataFrame({
    "A":[1,None,3,4],
    "B":[5,6,None,8],
    "C":[9,10,11,12]
})

print(df.dropna(subset=['A']))

#q2
# Drop rows where either A or B has missing values.

df = pd.DataFrame({
    "A":[1,None,3,None],
    "B":[5,6,None,8],
    "C":[9,10,11,12]
})

print(df.dropna(subset=['A' , 'B']))

#q3
# Drop rows where target column "Salary" is missing, but keep all others.

df = pd.DataFrame({
    "Age":[25,None,30,28],
    "Salary":[40000,50000,None,60000],
    "Experience":[2,3,5,4]
})
print(df.dropna(subset=['Salary']))


### Topic 1.2.5 — thresh in dropna()

# Concept
# df.dropna(thresh=n)
#
# Meaning:
# Keep rows that have at least n NON-missing values


# Data Set
# | Age | Salary | Experience |
# | --- | ------ | ---------- |
# | 25  | 40000  | 2          |
# | NaN | 50000  | 3          |
# | 30  | NaN    | 5          |
# | 28  | 60000  | 4          |

# Case 1
# df.dropna(thresh=3)
# Rule:
# Keep row only if it has 3 non-NaN values

# | Age | Salary | Experience |
# | --- | ------ | ---------- |
# | 25  | 40000  | 2          |
# | 28  | 60000  | 4          |


#Case 2
# df.dropna(thresh=2)
# Rule:
# Keep row if it has at least 2 valid values

# | Age | Salary | Experience |
# | --- | ------ | ---------- |
# | 25  | 40000  | 2          |
# | NaN | 50000  | 3          |
# | 30  | NaN    | 5          |
# | 28  | 60000  | 4          |






