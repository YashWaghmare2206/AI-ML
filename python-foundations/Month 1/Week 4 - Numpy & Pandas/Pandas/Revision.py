import pandas as pd
import numpy as np
from pandas.core.indexing import check_dict_or_set_indexers

###  🔹 TOPIC 1: Pandas Series — Core Fundamentals

# 1️⃣ What a Series really is (mental model)
# A Pandas Series is:
# A 1-D NumPy array + explicit labels (index)
#
# So it behaves like:
# a dictionary (key → value)
# an array (vectorized ops)
# That’s why it’s powerful for data analysis.


# 2️⃣ Why Series ≠ Python Dictionary
# You explicitly covered this difference:
#
# | Feature           | Series           | Dictionary    |
# | ----------------- | ---------------- | ------------- |
# | Custom index      | ✅                | ❌ (keys only) |
# | Math ops          | ✅                | ❌             |
# | Stats (mean, sum) | ✅                | ❌             |
# | NaN handling      | ✅                | ❌             |
# | Vectorized        | ✅ (NumPy-backed) | ❌             |
# | Used in DataFrame | ✅                | ❌             |
#
# Dictionary = storage
# Series = computation + analysis

# 3️⃣ Creating a Series (YOUR examples)
# 🔹 From list + custom index

list1 = [65 , 66 ,67 ,68, 69 , 70]
index = [11 , 12, 13 , 14 , 15 ,16]
s1 = pd.Series(list1 , index = index , dtype="float64")
print(s1)

# Key takeaways:
# Index can be anything (not 0…n)
# Index does not need to be continuous
# dtype forces uniform data type

# 🔹 From list without index

s2 = pd.Series(list1)
print(s2)
# Default index → 0,1,2,3…
#
# Still a Series, but label = position here


# 🔹 From dictionary
dict2 = {"a": 96, "b": 97, "c": 98, "d": 99, "e": 100}
s3 = pd.Series(dict2)
print(s3)

# Keys → index
# Values → data
# Automatic alignment by label

# 4️⃣ Series as Dictionary (IMPORTANT)
#
# You used Series exactly like a dict:
#
# 'a' in data        # membership check
# data.keys()        # index labels
# data.items()       # (index, value)
# data['c'] = 1      # modify value

# Series feels like a dictionary, but acts like a NumPy array when doing math.

# 5️⃣ Index vs Position (FOUNDATIONAL)
# This is where many people mess up — you didn’t 👍
#
# Label-based slicing
#
# data['a':'c']
# Uses labels
# End label included
#
# Position-based slicing
#
# data[0:4]
# Uses Python positions
# End index excluded
#
# # 👉 Same syntax, different meaning
# # This is why .loc and .iloc exist.

# 6️⃣ .loc is mandatory when index ≠ position
#
# Your example:
a = s1.loc[13:15]   # .loc for labels
print(a)
#
# Why?
#
# Index = [11,12,13,14,15]
# a1[13:15] would be misinterpreted as positional
# .loc tells pandas: “use labels, not positions”


## Questions

# q1
s1 = pd.Series([10, 20, 30, 40] , index = ['a','b','c','d'] , dtype="int64")
print(s1)
print(s1.index)
print(s1.values) # .items() is used in loop for printing

#q2
s2 = pd.Series([5, 10, 15, 20], index=[2, 4, 6, 8])
print(s2.loc[4:8]) # here end label is included
print(s2[1:3]) # here end " 3 " is not included

#q3
d1 = {'a': 10, 'b': 20, 'c': 30}
s3 = pd.Series(d1)
s3 *= 2
s3.loc["b"] += 5
print(s3)








###  🔹 TOPIC 2: Series Slicing, Selection & Masking


# 1️⃣ Selection vs Masking (Big Picture)
# Selection
# → Choosing which elements to keep
#
# Masking
# → Using True / False conditions to decide what stays, changes, or hides
#
# In pandas:
# True  → keep / act
# False → drop / ignore / replace
# This logic applies everywhere in Series & DataFrames.

# 2️⃣ Boolean Masking — Selection (YOUR code)
#
# Your example:
s = pd.Series([10, 20, 30, 40, 50], index=['a','b','c','d','e'])
# Basic boolean selection
print(s[s > 25])
#
# What happens internally:
# s > 25 → produces a boolean Series
# pandas keeps only True positions

# 🧠 Key rule:
# series[condition] = filter rows


# 3️⃣ Boolean Masking with .loc (Best Practice)
#
# You mentioned this
ans =  s.loc[s % 20 == 0]
print(ans)

# Why .loc is preferred:
# Explicit label-based selection
# Safer when index is integers
# Clear intent

# Rule to lock in:
# If condition depends on values → use .loc


# 4️⃣ Masking for Modification (Critical Difference)
#
# Your code:
print(s)
s[s > 30] = 0
print(s)
# This is NOT filtering — this is editing the Series.
#
# Effect:
# Values > 30 are replaced
# Original Series is changed
#
# 🧠 Rule:
# series[condition] = value → modify in place


# 5️⃣ .mask() — Hide True Values
#
# Your example:
#
s.mask(s == 0)
#
# Behavior:
# Where condition is True → replaced with NaN
# Where False → kept
#
# Important effects:
# Integers → converted to float
# Data is hidden, not deleted
#
# With replacement:
t = s.mask(s == 0, other=-1) # Keeps the false value and replaces the true one
print(t)

# 🧠 Think:
# .mask() = “hide where True”



# 6️⃣.where() — Opposite of .mask()
#
# Your code:
t2 = s.where(s == 30, other=-3)  # Keeps the true value and replaces the false value with other
print(t2)
#
# Behavior:
# Keep values where condition is True
# Replace where False

# 🧠 Mental model:
# mask  → hide True
# where → hide False


# 7️⃣ Multiple Conditions & Negation
#
# Your examples:
a = s[(s > 20) & (s < 50)]  # use " & " because it check's element wise and not entire object as " and " does
print(a)
#
# Rules:
# Use & instead of and
# Wrap each condition in parentheses

# Negation:
# ~(s > 30)
# Meaning:
# NOT (s > 30)

# 8️⃣ Label-Based Masking
#
# Your code:
#
mask = s.index.isin(['a', 'e'])
r = s[mask]
print(r)
#
# What’s happening:
# Condition is applied on index
# Not on values
#
# Use when:
# Filtering specific labels
# Non-numeric logic



# 9️⃣ NaN-Based Masking
#
# Your example:
#
s2 = pd.Series([10, None, 30, None, 50])
s2[s2.isna()]
#
# Key points:
# None → NaN
# isna() returns boolean mask
# Very common in real datasets


## Questions

#q1
l1 = [5 , 10 ,  15 ,  20 ,  25]
i1 = ['a' , 'b' , 'c' , 'd' , 'e']
s = pd.Series(l1 , index= i1)

a1 = s[s > 12]
a2 = s[s <= 15]
print(a1)
print(a2)

#q2
s1 = pd.Series([10, 20, 30, 40, 50])
a3 = s1.loc[s1 % 2 == 0]  # it always work on the existing data the view an not on copy as  a3 = s1[s1 % 2 == 0]
print(a3)
# a3 = s1[s1 % 2 == 0] this way may return copy when the memory is not continuous
a4 = s1[~(s1 > 30)]
print(a4)

#q3
s2 = pd.Series([1,2,3,4,5])
a5 = s2.mask(s2 > 3 , other=0)
print(a5)

#q4
s5 = pd.Series([10, 15, 20, 25, 30], index=['a','b','c','d','e'])
a6 = s5[(s5 >= 15) & (s5 <= 25)]
print(a6)
s5[s5 > 20] = -1
print(s5)
a8 = s5.mask(s5 == -1 , other=None)  # none here means Nan in Series # mask  always returns an copy of original series
print(a8)


#q5
s6 = pd.Series([100, 200, 300, 400, 500], index=['p','q','r','s','t'])
mask = s6.index.isin(['p' , 'r' , 't'])
a9 = s6[mask]
print(a9)
a10 = s6[s6 < 300]
print(a10)

#q6
s7 = pd.Series([10, None, 30, None, 50])
mask = s7.isna()
a11 = s7[mask]
print(a11)
s7[mask] = -99
print(s7)
mask2 = ~(s7.isna())
print(s7[mask2])

#q7
s8 = pd.Series([5, 10, 15, 20, 25, 30])
a12 = s8[(s8 > 10) & (s8 < 30)]
print(a12)
a12.loc[a12 > 20] = 100  # here we use .loc() memory is not continuous as s8 we have a12 which is filtered
print(a12)


#q8
s9 = pd.Series([10, 20, 30, 40], index=['a','b','c','d'])
a13 = s9.where(s9 == 20)  # .where() keeps true value same as it is and changes the false value to Nan or other = ..
print(a13)
a13.loc[a13 != 20] = -1 # just writing a13 in the .loc() gives error as .loc() expect labels or booleans or positions(indexs)
print(a13)  # also valid: s9.where(s9 == 20 , other = -1)


#q9
s10 = pd.Series([1,2,3,4,5,6])
a14 = s10.loc[s10 % 2 != 0]
print(a14)
a15 = a14.mask(a14 > 4)  # were condn is true the value becomes Nan
print(a15)


#q10
s10 = pd.Series([10, 20, 30], index=[1, 2, 3])
a16 = s10.loc[2:3]
print(a16)
a17 = s10.iloc[1:3]
print(a17)


###   🔹 TOPIC 3: Fancy Indexing + .loc vs .iloc (Series → DataFrame Bridge)

# 1️⃣ What is Fancy Indexing? (Big Picture)
#
# Fancy indexing = selecting multiple non-continuous elements at once
#
# Instead of:
# one slice → continuous block
#
# You do:
# multiple specific picks → scattered selection
# This exists because real data is not continuous.


s1 = pd.Series([10 , 20 , 30 ,40 , 50] , index= ['a' , 'b' , 'c' , 'd' , 'e'])

# 2️⃣ Fancy Indexing in Series — YOUR examples

# 🔹 By labels
# Your code:
r = s1[['a', 'b', 'e']]
print(r)
#
# What happens:
# You pass a list of labels
# Pandas returns values in that exact order
# Missing labels → error
#
# 🧠 Key rule:
# Fancy indexing always returns a new Series


# Series
#
# 🔹 By positions

r1 = s1.iloc[[0, 2, 4]]
print(r1)
#
# What’s important:
# .iloc expects positions
# Order matters
# Repetition is allowed
#
# Example:
# s.iloc[[2, 2, 0]]


# 3️⃣ Fancy Indexing vs Boolean Masking (DO NOT MIX)

# | Feature                  | Fancy Index | Boolean Mask |
# | ------------------------ | ----------- | ------------ |
# | List of labels/positions | ✅           | ❌            |
# | True/False condition     | ❌           | ✅            |
# | Order control            | ✅           | ❌            |
# | Repetition               | ✅           | ❌            |

# 🧠 Think:
#
# Fancy → “I know exactly what I want”
# Mask → “Give me what matches condition



# 4️⃣ .loc vs .iloc — Deep Understanding
#
# You already know basics; here’s what matters in practice.
#
# .loc
#
# Label-based

# Accepts:
# single label
# list of labels
# boolean mask
# Slice end included
#Exmpale
# s.loc[['a','c']]
# s.loc[s > 10]
# .iloc


# Position-based
#
# Accepts:
# integers
# list of integers
# Slice end excluded
#
# ❌ Does NOT accept boolean Series directly
#
# s.iloc[[0,2]]
# s.iloc[1:4]


# 5️⃣ Integer Index Trap (CRITICAL)
#
# Example:
#
# s = pd.Series([10,20,30], index=[1,2,3])
# Code	Meaning
# s[1]	❓ ambiguous
# s.loc[1]	label 1
# s.iloc[1]	position 1

# 🧠 Rule:
# If index is integer → always use .loc / .iloc



## Questions

#q1
s1 = pd.Series([10 , 20 , 30 ,40 , 50] , index= ['a' , 'b' , 'c' , 'd' , 'e'])
print(s1.loc[['a' , 'c' , 'e']])
print(s1.iloc[[0 , 2 , 4]])

#q2
s2 = pd.Series([5, 15, 25, 35], index=['w','x','y','z'])
print(s2.loc[['x' , 'z']])
print(s2.iloc[[1 , 3]])

#q3
s3 = pd.Series([100, 200, 300, 400], index=[10, 20, 30, 40])
print(s3.loc[[20 , 40]])
print(s3.iloc[[1 , 3]])

#q4
s4 = pd.Series([1,2,3,4,5])
print(s4.iloc[[4 , 2 , 0]])
print(s4.loc[s4 > 2])

#q5
s5 = pd.Series([5, 15, 25, 35], index=['w','x','y','z'])
print(s5)
print(s5.loc[['x' , 'w']])

#q6
s6 = pd.Series([10,20,30,40,50], index=[1,2,3,4,5])
print(s6.loc[[2,4,5]])
s6.iloc[[1,3,4]]   # positions corresponding to 2,4,5 labels
#q7
s7 = pd.Series([100,200,300], index=[0,1,2])
print(s7[[1,2]])
print(s7.loc[[0,1,2]])
print(s7.iloc[[0,1,2]])


#q8
s8 = pd.Series([7,14,21,28,35])
a1 = s8.iloc[[1,3]]
print(a1)
a2 = a1[a1 > 20]
print(a2)



###   🔹 TOPIC 4: DataFrame as Dictionary + Array (Row & Column Selection)


# 1️⃣ How to Think About a DataFrame (VERY IMPORTANT)
#
# A DataFrame = dictionary of Series
# column_name → Series
# row index   → label shared by all Series
#
# That’s why this works:
# df['Salary']
#
# You are literally pulling out a Series.

# 2️⃣ Your DataFrame Example (Revisiting)

salary = {"Rahul":45000, "Priya":60000, "Amit":52000, "Neha":48000, "Karan":70000}
positions = {
    "Rahul":"Software Engineer",
    "Priya":"Data Analyst",
    "Amit":"Backend Developer",
    "Neha":"HR Manager",
    "Karan":"Project Manager"
}
bonus = {"Rahul":15, "Priya":25, "Amit":20, "Neha":15, "Karan":10}

company = pd.DataFrame({
    "Salary": salary,
    "Positions": positions,
    "Bonus_percent": bonus
})

# Key thing:
# Pandas aligns data by row index (names)
# Order doesn’t matter in dicts


# 3️⃣ Column Selection (Dictionary Style)
df = company['Salary']   # ✔ Returns a Series
print(df)
df = company[['Salary', 'Bonus_percent']]
print(df)

# 🧠 Rule:
# One label → Series
# List of labels → DataFrame


# 4️⃣ Creating & Modifying Columns
#
# Your code:
#
company['Bonus'] = (company['Salary'] * company['Bonus_percent']) / 100
#
# Important points:
# Vectorized column-wise operation
# Index alignment preserved
# New column auto-added


# 5️⃣ Accessing Index & Values
# company.index      # row labels
# company.values     # numpy array (2D)
#
# 🧠 Caution:
# .values loses column names & index
# Use for computation, not logic


# 6️⃣ DataFrame as Array
# Transpose

print(company.T)
#
# Rows ↔ columns

# .iloc (array-style indexing)
a1 = company.iloc[:2, :3]
print(a1)
#
# Meaning:
# First 2 rows
# First 3 columns
# End index excluded


# 7️⃣ Modifying DataFrame Values
#
# Your code:
company.iloc[0, 3] = 70000

# 🧠 Meaning:
# Row 0 → Rahul
# Column 3 → Bonus
# Value replaced safely


# 8️⃣ Row Selection (VERY IMPORTANT)
# Slice rows (position-based)
# company[1:2]
#
# ⚠ Works, but not recommended
# Better:
#
# company.iloc[1:2]
# Conditional row selection
t = company[company.Salary > 50000]
print(t)

# Returns:
# Filtered DataFrame
# Condition applied row-wise


## Questions

import pandas as pd

salary = {"Rahul":45000, "Priya":60000, "Amit":52000, "Neha":48000, "Karan":70000}
positions = {
    "Rahul":"Software Engineer",
    "Priya":"Data Analyst",
    "Amit":"Backend Developer",
    "Neha":"HR Manager",
    "Karan":"Project Manager"
}
bonus = {"Rahul":15, "Priya":25, "Amit":20, "Neha":15, "Karan":10}

company = pd.DataFrame({
    "Salary": salary,
    "Position": positions,
    "Bonus_percent": bonus
})

#q1
print(company['Salary'])
print(company[['Salary' , 'Bonus_percent']])

#q2
print(company.index)
print(company.values)

#q3
print(company.iloc[:2])
print(company.iloc[-2:])   # It always [leftmost : rightmost] # gere it is 2nd lat to last


#q4
print("------------------------")
ans = company.loc[company.Salary > 50000]
print(ans)
ans1 = ans[['Salary' , 'Position']]
print(ans1)


#q5
print("------------------------")
a1 = company.iloc[1]
print(a1)
a2 = company.loc['Priya']
print(a2)


#q6
print("------------------------")
company['Bonus'] = company['Salary'] * company['Bonus_percent'] / 100
print(company)

#q7 (Important Question)
print("------------------------")
company.loc[(company.Salary > 48000 ) &  (company.Salary <= 65000 ) , 'Bonus_percent'] = 30
print(company)
# The .loc property is the "Laser Pointer" of Pandas. It takes two arguments: [row_indexer, column_indexer].
# Rows: It uses the Boolean Mask we created above to identify exactly which rows to target.
# Columns: It targets the 'Bonus_percent' column specifically for those rows.



#q8
print("------------------------")
a = company.loc[company['Position'].str.contains("Manager") , ['Salary' , 'Bonus_percent']]
print(a)


#q9

a1 = company[1:3]
print(a1)
a2 = company.iloc[1:3]
print(a2)


#q10

print("------------------------")
company['Salary'] = company['Salary'].astype(float)
company.loc[company['Salary'] > 50000, 'Salary'] *= 1.10
print(company)





### 🔹 TOPIC 5: DataFrame Indexing & Alignment (Deep Understanding)

# 1️⃣ Index Alignment — THE CORE IDEA
# Golden rule (lock this 🔒):
#
# Pandas aligns data by labels, not by position

# This is true for:
#
# Series vs Series
# DataFrame vs Series
# DataFrame vs DataFrame

s1 = pd.Series([10, 20, 30], index=['a','b','c'])
s2 = pd.Series([1, 2, 3], index=['b','c','d'])

s3 = s1 + s2
print(s3)

# What pandas does internally:
# Index  s1   s2
# a      10   NaN
# b      20   1
# c      30   2
# d      NaN  3
## Result
# a    NaN
# b    21
# c    32
# d    NaN

# 🧠 Key insight
# Pandas does set-style alignment, not array-style addition.


# 2️⃣ Why Alignment Exists (Design Reason)
#
# If pandas used positions:
#
# Data from different sources would silently mix
# Results would be wrong without warning
#
# Alignment gives:
#
# Safety
# Correctness
# Transparency
# This is why pandas is trusted in data science.


# 3️⃣ DataFrame Alignment (Column-wise)

df1 = pd.DataFrame({
    'A': [1,2],
    'B': [3,4]
})

df2 = pd.DataFrame({
    'B': [10,20],
    'C': [30,40]
})

print(df1 + df2)

# alignment happens on:
# Rows (index)
# Columns (labels)


# 4️⃣ Reindexing — Explicit Alignment Control
# What is reindex()?
#
# Force pandas to follow a specific index or column order

s = pd.Series([10,20,30], index=['a','b','c'])
s2 = s.reindex(['b','c','d'])
s3 = s.reindex(['b','c','d'], fill_value=0)  # fill_value replaces the Nan value with 0
# and NaN is an floating point number so to fit it in column everything is converted to float64
print(s2)
print(s3)

# 🧠 Pandas did NOT guess values — it inserted NaN.

# .reindex()  # it returns an copy
# 1. It Rearranges (Reordering)
# If you have an index ['a', 'b', 'c'] and you reindex to ['c', 'a', 'b'], it moves the data to match that specific order. It’s a very fast way to sort or custom-order your rows.
#
# 2. It Inserts (Expanding)
# If you provide a label that wasn't there before (like your 'd' example), it creates a new row and fills it with NaN. This is useful when you have a list of "Expected Categories" and you want to see which ones are missing from your data.
#
# 3. It Filters (Shrinking)
# If you leave a label out of your new list (like you left out 'a'), it drops that row from the result.


# 5️⃣ Reindexing DataFrames
# Rows
a =  company.reindex(['Rahul','Neha','Unknown'])
# Columns
b = company.reindex(columns=['Salary','Bonus_percent'])
print(a)
print(b)
#
# 🧠 Rule:
# Missing labels → NaN
# Extra labels → ignored unless re-indexed

# 6️⃣ Renaming Index & Columns

# Rename columns
a = company.rename(columns={'Salary':'CTC'})

# Rename index
b = company.rename(index={'Rahul':'Rahul S'})

# ⚠ By default, this returns a new DataFrame
#
# Use:
# company.rename(..., inplace=True)
# only if you’re sure.


# 7️⃣ Setting & Resetting Index

# set_index()       # Returns a new object can be dataframe or an series depends
# Turns a column into row index:
d = company.set_index('Position')
print(d)

# reset_index()     # Returns a new object can be dataframe or an series depends
# Brings index back as a column:
company.reset_index()  # it Stores the previoius index an an new column called 'index' and stored in dataframe
print(company)

# 🧠 Index = label system, not data storage.


## Question

#q1
s1 = pd.Series([10, 20, 30], index=['a','b','c'])
s2 = pd.Series([1, 2, 3], index=['b','c','d'])

s3 = s1 + s2
print(s3)

#q2
s = pd.Series([100, 200, 300], index=['x','y','z'])
a = s.reindex(['y' , 'z' , 'a'] , fill_value = 0)  # when fill_value is used the dtype of elements are same as they were
print(a)

#q3
print(company.index)
print(company.columns)

#q4
df1 = pd.DataFrame({
    'A': [1,2],
    'B': [3,4]
})

df2 = pd.DataFrame({
    'B': [10,20],
    'C': [30,40]
})
d = df1 + df2
print(d)


#q5
a = company.reindex(['Rahul','Neha','Unknown'])
b = company.reindex(columns = ['Salary','Bonus_percent','Bonus'])
print(a)
print(b)


#q6
a = company.rename(columns = {'Salary' : "CTC"}) # unless using inplace = True .rename() also return an new Dataframe
print(a)
b = company.rename(index = {'Priya' : "Priya P"})
print(b)


#q7
s = pd.Series([5,10,15], index=['a','b','c'])
a = s.reindex(['c','b','a','d'] , fill_value=-1)
print(a)

#q8
a = company.set_index("Position")
print(a)
b = a.reset_index()
print(b)


#q9
a = company + company[['Salary']]  # The salary is doubled all other Nan
print(a)

#q10
company.loc[: , 'Salary'] += 5000
print(company)





###  🔹 TOPIC 6: Sorting & Ranking (Practical & Very Common

# 1️⃣ Two Types of Sorting (Big Picture)
#
# In pandas, you can sort by:
# Values → sort_values()
# Index (labels) → sort_index()

# They are completely different operations.

# 2️⃣ Sorting by VALUES (sort_values)
#
# Using your company DataFrame.
#
# Sort by Salary (ascending)
a = company.sort_values(by='Salary')
print(a)
# Sort by Salary (descending)
b = company.sort_values(by='Salary', ascending=False)
print(b)
#
# 🧠 Important:
# Sorting returns a new DataFrame
# Original is unchanged unless inplace=True


# 3️⃣ Sorting by MULTIPLE Columns
# Example:

a = company.sort_values(
    by=['Bonus_percent', 'Salary'],
    ascending=[False, True]
)
print(a)

# Meaning:
# Sort by Bonus_percent (high → low)
# If tie → sort by Salary (low → high)

# Primary Sort: It sorts the entire table by Bonus_percent from Highest to Lowest (because of False).
# Secondary Sort: Only if two people have the same bonus (e.g., both have 15%), it will look at their salaries and put the Lower Salary first (because of True).
# If you have three columns, the 3rd column acts as the tie-breaker for the tie-breaker.


# 4️⃣ Sorting by INDEX (sort_index)
# Row index sort
a = company.sort_index()
print(a)
# Reverse index
b = company.sort_index(ascending=False)
print(b)
#
# 🧠 Index sorting does not look at values, only labels.


# 5️⃣ Sorting Series vs DataFrame
# Series
# company['Salary'].sort_values()
# company['Salary'].sort_index()
# DataFrame
# company.sort_values(by='Salary')
# company.sort_index()
#
# Same idea, different structure.


# 6️⃣ Ranking (VERY IMPORTANT CONCEPT)
#
# Ranking assigns relative order instead of rearranging data.
#
a = company['Salary'].rank()
print(a)
company['Salary'].rank(ascending=False)
#
# Output:
# Lowest value → rank 1
# Highest → largest rank'

# Handling ties (method)

# company['Salary'].rank(method='average')
# Name,Salary,Rank
# Priya,"60,000",1.5
# Amit,"60,000",1.5
# Rahul,"50,000",3.0

# company['Salary'].rank(method='min')
# Name,Salary,Rank
# Priya,"60,000",1.0
# Amit,"60,000",1.0
# Rahul,"50,000",3.0

# company['Salary'].rank(method='dense')
# Name,Salary,Rank
# Priya,"60,000",1.0
# Amit,"60,000",1.0
# Rahul,"50,000",2.0

# Method	Meaning
# average	average rank
# min	lowest rank
# dense	no gaps


# 7️⃣ Sorting vs Ranking (Lock this 🔒)
# Sorting	                    Ranking
# Reorders rows	                Keeps order
# Moves data	                Adds info
# Changes index order	        Preserves index


## Questions

#q1
a = company.sort_values(by='Salary')
b = company.sort_values(by= 'Salary' , ascending=False)
print(a)
print(b)


#q2
a = company.sort_index()
b = company.sort_index(ascending=False)
print(a)
print(b)


#q3
a = company['Salary'].sort_values()  # Series Sorting
print(a)


#q4
a = company.sort_values(
    by=['Bonus_percent' , 'Salary'],
    ascending=[False , True]
)
print(a)


#q5
company['Salary_Rank'] = company['Salary'].rank(ascending=False , method="dense")


#q6
a = company['Salary'].rank(ascending=False , method='average')
b = company['Salary'].rank(ascending=False , method='dense')
print(a)
print(b)


#q7
a = company.sort_values(by = 'Salary')
b = a.reset_index()
print(b)


#q8

company = company.sort_index()
company['Index_Rank'] = company.index.to_series().rank()
print(company)


#q9
a = company.sort_values(by = 'Salary')
b = company['Salary'].rank()
print(a)
print(b)

#q10

company['Salary_Rank'] = company['Salary'].rank(ascending=False , method="dense")
company = company.sort_values(by = 'Salary_Rank')
print(company[['Salary' , 'Salary_Rank']])










