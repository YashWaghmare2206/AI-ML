import pandas as pd
import numpy as np

##Series

# Series is from pandas, dictionary is built-in Python
# Series supports custom index (user-defined labels)
# Series supports mathematical operations
# Series has statistical functions (mean, sum, etc.)
# Series handles missing values (NaN)
# Series supports index-based slicing
# Series is faster for large data (NumPy-based)
# Series integrates with DataFrame
# Dictionary is for general storage, Series is for data analysis


list1 = [65, 66, 67, 68, 69]
dict1 = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E"}
dict2 = {"a": 96, "b": 97, "c": 98, "d": 99, "e": 100}
index = [11, 12, 13, 14, 15]  # index can be anything string or non continuous number
# Creation of Series

a1 = pd.Series(list1,
              index=index , dtype = "float64")  # Here the syntax is p.Series(a , index = b) here "a" can be dict list of [1,2,3,] and "b" is the new labels or indedx you have to give to list
a2 = pd.Series(list1)

# Base index                         # Series is also called 1 dimensional numpy array
print(a1)
# Updated label or index name
print(a2)
# Slicing
print(a1.loc[13:15]) # Cannot write a1[13:15] as python will see 13:15 has actual index


                                                        ## DataFrame

# Constructor
#  pd.DataFrame(data=None, index=None, columns=None)

# data → The actual data used to create the DataFrame (dict, list, array, Series, etc.)
# index → Labels for the rows (row names)
# columns → Labels for the columns (column names)
# dtype → Forces a specific data type for all columns
# copy → If True, copies data instead of referencing original
# Number of keys in data = number of columns created.
# columns= decides which of those columns to show and in what order.

# We can name column using column=[] only when data doesn't have any name from first

b1 = pd.DataFrame({"Capital Value":dict1  , "Ascii Value": dict2}) # Here DatFrame is called 2d array an and values come together by common label in this case the labels are (a,b,c,d,.e)
print(b1)

print(b1['Ascii Value'])


## Constructing DataFrame Objects


### The `columns` Parameter in One-Line Summaries

# With a Dictionary:** It acts as a **filter/selector** that only keeps data where the dictionary keys exactly match the names in your list.
# With a Series:** It acts as a **labeler** that assigns a name to the single column of data being converted.
# With a List of Lists:** It acts as a **header-mapper** that assigns names to each column based on their numerical order (0, 1, 2...).
# With a List of Dicts:** It acts as a **reorderer/schema** that picks specific keys and arranges them in the sequence you provided.



# From Single Series Object

s1 = pd.Series(dict1)
print(s1)
c1 = pd.DataFrame(b1 , columns=['Capital'])
print(c1)


# From List of Dicts

data = {chr(i) : i  for i in range(65,90)}
d1 = pd.DataFrame([data])                                 # No need to store it will convert it in place
print(d1)

# ## ✅ Case 1: `pd.DataFrame(data)`  (or `(data)`)
#
# ```python
# data = {'A': 65, 'B': 66, 'C': 67}
# pd.DataFrame(data)
# ```
# ### What pandas thinks:
#
# * Input is a **dict**
# * Dict keys → **column names**
# * Dict values → **data for columns**
#
# But your values are **scalars**, not lists.
#
# So pandas internally treats each scalar like:
#
# ```text
# A → row 0
# B → row 1
# C → row 2
# ```
#
# ### Result:
#
# * Each column gets **one value at a different row**
# * Everything else is missing → `NaN`
#
# ➡️ **Diagonal matrix effect**
#
# ✔ Your explanation:
#
# > every element in dict has 0 to n index and every key is column name
#
# That’s conceptually right.

# ## ✅ Case 2: `pd.DataFrame([data])`
#
# ```python
# pd.DataFrame([data])
# ```
#
# ### What pandas thinks:
#
# * Input is a **list**
# * Each list element → **one row**
# * That row happens to be a dict
# * Dict keys → **column names**
# * Dict values → **values in that row**
#
# Since:
#
# * list has only **one index: 0**
# * dict contains **all columns**
#
# ➡️ You get **one clean row**
#
# ---
#
# ## 🧠 One-line mental rule (lock this in)
#
# > **`data` → columns-first interpretation
# > `[data]` → rows-first interpretation**
#
# ---
#
# ## 🔑 Even more precise rule
#
# | Expression | Pandas interpretation |
# | ---------- | --------------------- |
# | `data`     | dict of columns       |
# | `(data)`   | same as `data`        |
# | `[data]`   | list of rows          |
# | `{k: [v]}` | column with one row   |
# | `{k: v}`   | diagonal trap ⚠️      |




# From Dictionary of Series Object

e1 = pd.DataFrame({"Capital Value":dict1  , "Ascii Value": dict2}) # Here DatFrame is called 2d array an and values come together by common label in this case the labels are (a,b,c,d,.e)
print(b1)

# From 2D Arrays

f1 = pd.DataFrame( np.random.rand(3,4) , columns=['First_col' , "Second_col" , "Third_col" , "Fourth_col"]) # You can give also index=[23 , 45, 67]
print(f1)

# From an Numpy structured Array

A = np.zeros(3 , dtype=[('A' , 'i8') , ('B' , 'f8')]) # Here it generates 3 eleemnts like tuple first (A_value , B_value)
print(A)
f2 = pd.DataFrame(A)
print(f2)               # First column is A and Second is B

# Pandas Index Object

ind = pd.Index([2,3,5,7,11]) # They are index od Series object and in Dataframe it is label of rows
print(ind)
# Index are immutable
# e1.index[0] = 'z'    # This not possible
# e1.index = ['x', 'y', 'z']  # replace whole index is possible

# We can Perform all Sets related method union , intersection , differences etc















