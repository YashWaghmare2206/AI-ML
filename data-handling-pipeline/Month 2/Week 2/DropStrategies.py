
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




                            # Section 1.3 — Fill Strategies

# Topic 1.3.1 — df.fillna()


# 1️⃣ Concept
# df.fillna(value)
#
# Meaning:
# Replace all missing values (NaN) with the given value
#
# 2️⃣ Our Base Dataset (same one)
# df = pd.DataFrame({
#     "Age":[25,None,30,28],
#     "Salary":[40000,50000,None,60000],
#     "Experience":[2,3,5,4]
# })
# Row	Age	Salary	Experience
# 0	25	40000	2
# 1	NaN	50000	3
# 2	30	NaN	5
# 3	28	60000	4
# 3️⃣ Example 1 — Fill with 0
#     df.fillna(0)
#
# Output:
#
# Age	Salary	Experience
# 25	40000	2
# 0	50000	3
# 30	0	5
# 28	60000	4
#
# Meaning:
# All NaN → replaced by 0
# 4️⃣ Example 2 — Fill with Specific Value
# df.fillna("Missing")
#
# Possible for object/text columns.
#
# Example:
# df["City"].fillna("Unknown")
#
# Used often for:
# City
# Gender
# Category
# Department

# 5️⃣ Important Detail
# ⚠ fillna() does NOT change original dataframe   # Important
#
# Example:
# df.fillna(0)
# print(df)
#
# Original remains same.
#
# To save permanently:
#
# df = df.fillna(0)
# or
# df.fillna(0, inplace=True)

# 6️⃣ Real ML Insight
#
# Suppose:
# Age missing
#
# Using:
# df.fillna(0)
# means
# Age = 0 years old
# This may be wrong logically.

# 7️⃣ Very Useful Version
#
# Fill only specific column:
# df["Age"] = df["Age"].fillna(0)
# Better than filling whole dataframe.



#q1
# Fill all missing values with 0
df.fillna(0)

#q2
#Fill only the Age column with 0
df['Age'] = df['Age'].fillna(0)

# q3
clean_df = df.fillna(-1)

#Q4
# Missing values before: X
# Missing values after fillna(0): Y

print(df)
print(df.fillna(0))


#q5
# Fill only Salary missing values with:
df["Salary"] = df["Salary"].fillna(99999)
print(df)

# Q6

df.fillna(100 , inplace=True)




# Topic 1.3.2 — Mean vs Median Filling

# 1️⃣ Mean Filling
# Concept
# df["column"].fillna(df["column"].mean())
#
# Meaning:
# Replace missing values using the average value of that column

# Our Base Dataset
df = pd.DataFrame({
    "Age":[25,None,30,28],
    "Salary":[40000,50000,None,60000],
    "Experience":[2,3,5,4]
})
# | Row | Age | Salary | Experience |
# | --- | --- | ------ | ---------- |
# | 0   | 25  | 40000  | 2          |
# | 1   | NaN | 50000  | 3          |
# | 2   | 30  | NaN    | 5          |
# | 3   | 28  | 60000  | 4          |

# 2️⃣ Example — Mean Fill for Age
df["Age"] = df["Age"].fillna(df["Age"].mean()) # (25 + 30 + 28) / 3 = 27.67
print(df)

# 3️⃣ Median Filling
# Concept
# df["column"].fillna(df["column"].median())
# Meaning:
# Replace missing values using the middle value

df["Age"] = df["Age"].fillna(df["Age"].median())

# 4️⃣ Mean vs Median (Very Important)
# | Method | Best Used When                    |
# | ------ | --------------------------------- |
# | Mean   | data is normal / no big outliers  |
# | Median | data has outliers / skewed values |

# 5️⃣ Example of Outlier Problem
#
# Suppose Salary values:
# 40000, 50000, 60000, 5000000

# Mean
# Very large → unrealistic
# because 50 lakh distorts average.
#
# Median
# Middle value remains stable
# Much safer.

# 6️⃣ Real ML Rule
# Numerical + no outliers → Mean
# Numerical + outliers → Median
# Categorical → Mode
# This is a common interview question.




# Topic 1.3.3 — Mode Filling + Forward Fill + Backward Fill

# Part 1 — Mode Filling

# 1️⃣ Concept
# df["column"].fillna(df["column"].mode()[0])
#
# Meaning:
# Replace missing values using the most frequently occurring value
#
# This is mainly used for:
# Categorical columns
# like:
# Gender
# City
# Department
# Category
# Product Type

# 2️⃣ Example
# df = pd.DataFrame({
#     "City":["Mumbai", "Pune", None, "Mumbai", "Delhi"]
# })
#
# Values:
# Mumbai, Pune, Mumbai, Delhi
# Most frequent value:
# Mumbai
#
# So:
# df["City"] = df["City"].fillna(df["City"].mode()[0])
# Missing value becomes:
# Mumbai

# 3️⃣ Why [0] ?
#
# Because:
# df["City"].mode()
# returns a Series, not a single value.
#
# Example:
# 0    Mumbai
# dtype: object
# So we use:
# .mode()[0]


# Part 2 — Forward Fill (ffill)

# 4️⃣ Concept
# df.fillna(method="ffill")
# or modern/common form:
#
# df.ffill()
# Meaning:
# Fill missing value using the value just before it

df = pd.DataFrame({
    "Sales":[100, None, None, 250]
})

#Original
# | Sales |
# | ----- |
# | 100   |
# | NaN   |
# | NaN   |
# | 250   |
                # After ffill()
# Output
# | Sales |
# | ----- |
# | 100   |
# | 100   |
# | 100   |
# | 250   |

# 5️⃣ Use Case
#
# Very useful in:
# Time series data
# Stock prices
# Sensor data
# Daily reports


# Part 3 — Backward Fill (bfill)

# 6️⃣ Concept
# df.fillna(method="bfill")
# or
# df.bfill()
# Meaning:
# Fill missing value using the next available value

# 7️⃣ Difference Between ffill and bfill
# Method	Uses
# ffill()	previous value
# bfill()	next value

# 8️⃣ Real ML Rule
# | Column Type             | Best Fill Method |
# | ----------------------- | ---------------- |
# | Numerical normal        | Mean             |
# | Numerical with outliers | Median           |
#     | Categorical             | Mode             |
# | Sequential/Time Data    | ffill / bfill    |


# Example for Solving

# Q1
# Fill missing values in Department using mode

df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

# Q2
# Use forward fill for the whole dataframe
df = df.fillna(method='ffill')

# Q3
# Use backward fill for the whole dataframe and store result in:
clean_df = df.fillna(method='bfill')

# Q4
# Print: Mode of Department: X
print(df['Department'].mode()[0])

# Q5
# Fill only Salary using forward fill
df['Salary'] = df['Salary'].fillna(method = 'ffill') # df["Salary"] = df["Salary"].ffill() Series suports ffill

# 6 (Interview-style)
# Which is better for:
# Daily stock prices with missing dates
# Mean, Median, Mode, or Forward Fill?
# Ans : Forward Fill



                    # Section 1.4 — Advanced Fill Techniques

# Topic 1.4.1 — interpolate() 🔥 Interpolation

# 1️⃣ Concept
# df.interpolate()
#
# Meaning:
#
# Fill missing values by estimating values using surrounding data
#
# Usually used for:
#
# time series
# stock prices
# temperature
# sales trends
# sensor readings
#
# 2️⃣ Simple Example
# df = pd.DataFrame({
#     "Sales":[100, None, None, 160]
# })
# Original:
# Row	Sales
# 0	100
# 1	NaN
# 2	NaN
# 3	160
# 3️⃣ Normal fillna() vs Interpolation
# If we use forward fill
# df.ffill()
#
# Output:
# Sales
# 100
# 100
# 100
# 160
#
# This ignores the trend.
#
# If we use interpolation
# df.interpolate()

# Output:
# Sales
# 100
# 120
# 140
# 160
#
# Because pandas estimates:
#
# increase is gradual

# 4️⃣ How It Thinks
#
# From:
# 100 → 160
#
# Difference:
# 60
# There are:
# 3 steps
# So:
# 60 / 3 = 20
# Then:
# 100
# 120
# 140
# 160

# 5️⃣ Syntax
# df.interpolate(method="linear")
# Default is usually:
# linear interpolation
# which means:
# straight-line estimation

# 6️⃣ Real ML Example
# Suppose:
# Temperature data
# Day	Temp
# Mon	30
# Tue	NaN
# Wed	NaN
# Thu	36
#
# Mean fill gives:
# 33
# 33
# But interpolation gives:
# 32
# 34
# Much better.

# 7️⃣ Important Limitation
#
# Interpolation works best for:
# ✔ continuous numeric data
#
# Not good for:
# ❌ names
# ❌ gender
# ❌ city
# ❌ categories
#
# Because:
# You cannot interpolate "Mumbai"
# 8️⃣ Common Interview Question
# Which is better?
# mean fill vs interpolation
#
# Answer:
# For time-based gradual data → interpolation is better


# Section 1.4.2 — Group-Based Fill

# 1️⃣ Why Normal Mean Can Be Wrong
# Suppose dataset:
#
# Department	Salary
# IT	50000
# IT	NaN
# HR	30000
# HR	NaN
#
# If we do:
# df["Salary"].fillna(df["Salary"].mean())
#
# Global mean:
# (50000 + 30000) / 2 = 40000
# Then both missing values become:
# 40000
# ⚠ Wrong because:
# IT salaries and HR salaries are different

# 2️⃣ Better Solution — Group Fill
# We fill using:
# IT average for IT rows
#     HR average for HR rows

df = pd.DataFrame({
    "Department":["IT","IT","HR","HR"],
    "Salary":[50000,None,30000,None]
})

# 3️⃣ Syntax
df["Salary"] = df.groupby("Department")["Salary"].transform(lambda x: x.fillna(x.mean()))

# df.groupby("Department")  # IT group  HR group
# ["Salary"] Focus only on Salary column.
#  transform(...) Apply operation and return same shape.This is important because:transform keeps row structurewhile: # agg()does not.
# lambda x: x.fillna(x.mean())  for each group, fill NaN using that group's mean

# 7️⃣ Real ML Use Cases
# Very common for:
#
# Salary by Department
# Marks by Class
# Income by City
# House price by Area
# Spending by Customer Type
#
# This is production-level preprocessing.


# 8️⃣ Interview Insight
# Question:
# Why use groupby fill instead of mean fill?
#
# Answer:
# Because different groups have different distributions
# Excellent interview point.
#



