import pandas as pd
import numpy as np

rng = np.random.default_rng(seed = 1701)
ind = ['a' , 'b' , 'c' , 'd' , 'e']
x = rng.integers(10 , size=5).astype(np.float32)   # .astype change dtype

data = pd.Series(x , index=ind)

print(data)

## Similar Dictionary like function

a1 = 'a' in data  # Check if an index exist in series
a2 = data.keys()  # All keys in the Series
a3 = data.items() # Returns tuple of key and values

data['c'] = 1   # Modification like dictionary
print(data)


## Series as one dimensional Array

# slicing by explicit index (the indexs we decided)
print(data['a' : 'c'])     # Here we are slicing using labels of series # here it works without .loc as a , c are string it is only used for integers  index
                           # Here the last string label is also included

# slicing by implicit index (the index python had default 0 to n)
print(data[ 0 : 4])        # Here index 4 is not included



##  Masking
s = pd.Series([10, 20, 30, 40, 50], index=['a','b','c','d','e'])
print(s)

# 1️⃣. Boolean masking (selection)
# Condition → keep True values
a1 = s[ s > 25 ]    # Filtering
print(a1)

# 2️⃣ Boolean masking with .loc (recommended)
a2 = s[s % 20 == 0]  # can also be s.loc[s % 20 == 0] # Filtering
print(a2)

# 3️⃣ Masking to modify values
s[s > 30] = 0   # Modifying the original series  # Modify
print(s)

# 4️⃣ .mask() method (hide values)
print(s.mask(s == 0))  # Filtering and hiding base don condition
# Here true values to NaN and  also int concerted to float

# 5️⃣️.mask() with replacement value
s.mask(s == 0 , other=-1)   # Replaces the true values with -1

# 6️⃣ .where() (opposite of mask)
s.where(s == 30 , other=-3)   # Were value is false their -3 returns the view

# 7️⃣ Multiple-condition masking
print(s[(s > 20) & (s < 50)])

# 8️⃣ Label-based masking
mask = s.index.isin(['a', 'e'])   # Filtering
print(s[mask])

# 9️⃣ NaN-based masking
s2 = pd.Series([10, None, 30, None, 50])
print(s2[s2.isna()])

# 🔟 Negated masking (~)
print(s[~(s > 30)])

# | Type                   | Purpose       |                  |
# | ---------------------- | ------------- | ---------------- |
# | `s[condition]`         | select        |                  |
# | `s.loc[condition]`     | safe select   |                  |
# | `s[condition] = value` | modify        |                  |
# | `s.mask()`             | hide True     |                  |
# | `s.where()`            | hide False    |                  |
# | `&`, `                 | `, `~`        | combine / negate |
# | `isna()`               | NaN masking   |                  |
# | `index.isin()`         | label masking |                  |


# Fancy Indexing

# With Labels
r = data[['a' , 'b' , 'e']]
print(r)

# With Positions
r1 = s.iloc[[0, 2, 4]]  # iloc used when we to say it to do position based slicing etc nor label based
print(r1)


## loc VS iloc

# | Feature                 | `.loc`        | `.iloc`        |
# | ----------------------- | ------------- | -------------- |
# | Basis                   | labels        | positions      |
# | Uses index names        | ✅             | ❌              |
# | End of slice            | **inclusive** | **exclusive**  |
# | Accepts boolean mask    | ✅             | ❌ (use `.loc`) |
# | Accepts fancy indexing  | ✅             | ✅              |
# | Integer index confusion | possible      | none           |




## DataFrame as Dictionary


salary = {"Rahul" : 45000 , "Priya": 60000 , "Amit": 52000 , "Neha": 48000 , "Karan": 70000}
positions = {
    "Rahul": "Software Engineer",
    "Priya": "Data Analyst",
    "Amit": "Backend Developer",
    "Neha": "HR Manager",
    "Karan": "Project Manager"
}
bonus = {
    "Rahul": 15,
    "Priya": 25,
    "Amit": 20,
    "Neha": 15,
    "Karan": 10
}

company = pd.DataFrame({"Salary" : salary , "Positions" : positions , "Bonus_percent": bonus})
print(company)
print()

# Making a column and performing arithmetic operation on existing columns
company['Bonus']  = (company['Salary'] * company["Bonus_percent"]) / 100
print(company)

# Accessing only index or values

# For all index
print(company.index)
# For only specific row index
print(company.index[0])

# For all values
print(company.values)
# For only specific row value
print(company.values[0])



# Can also apply Array like operation on DataFrame
print(company.T)


# For array style indexing
print(company.iloc[:2 , :3])  # We see only 2 rows 3 columns


# Changing value
company.iloc[0,3] = 70000  # [row , column]
print(company)

print()

# Row Slicing by index in DataFrame
print(company[1:2])

# Row Slicing by condition
print()
print(company[company.Salary > 50000])


