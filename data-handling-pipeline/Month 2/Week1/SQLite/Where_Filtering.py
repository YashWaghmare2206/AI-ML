
import sqlite3
import pandas as pd

# # 🔹 Topic 5 — WHERE Filtering
#
# Goal:
#
# > **Filter rows based on conditions**
#
# This is what turns SQL from “show everything” into **useful data extraction**.
#


#
# ## 1️⃣ WHERE with Comparison Operators
#
# ### Operators
#
# * `=` equal
# * `>` greater than
# * `<` less than
# * `>=`, `<=`
#
# ### Example
#
# ```sql
# SELECT * FROM sales
# WHERE price > 10000;
# ```
#
# Only rows with price above 10,000.
#


#
# ## 2️⃣ WHERE with AND / OR / NOT
#
# ### AND (all conditions must be true)
#
# ```sql
# SELECT * FROM sales
# WHERE price > 10000 AND quantity >= 2;
# ```
#
# ### OR (any condition true)
#
# ```sql
# SELECT * FROM sales
# WHERE product = 'Laptop' OR product = 'Phone';
# ```
#
# ### NOT
#
# ```sql
# SELECT * FROM sales
# WHERE NOT product = 'Speaker';
# ```
#


#
# ## 3️⃣ IN — Multiple Values (Cleaner than OR)
#
# ```sql
# SELECT * FROM sales
# WHERE product IN ('Laptop', 'Phone', 'Tablet');
# ```
#
# Same as:
#
# ```sql
# product = 'Laptop' OR product = 'Phone' OR product = 'Tablet'
# ```
#


# ## 4️⃣ BETWEEN — Range Filtering
#
# ```sql
# SELECT * FROM sales
# WHERE price BETWEEN 5000 AND 30000;
# ```
#
# 📌 `BETWEEN` is **inclusive** (5000 and 30000 included).
#



#
# ## 5️⃣ LIKE — Pattern Matching
#
# Used with `TEXT`.
#
# ### Wildcards
#
# * `%` → any number of characters
# * `_` → exactly one character
#
# ### Examples
#
# ```sql
# SELECT * FROM sales
# WHERE product LIKE 'S%';
# ```
#
# Products starting with **S**
#
# ```sql
# SELECT * FROM sales
# WHERE product LIKE '%phone%';
# ```
#
# Products containing **phone**
#



# ## 6️⃣ IS NULL — Missing Values
#
# ```sql
# SELECT * FROM sales
# WHERE quantity IS NULL;
# ```
#
# ⚠️ Never use `= NULL`
#
# ❌ Wrong:
#
# ```sql
# quantity = NULL
# ```


# ## 7️⃣ WHERE + ORDER + LIMIT (Real Pattern)
#
# ```sql
# SELECT product, price
# FROM sales
# WHERE price > 10000
# ORDER BY price DESC
# LIMIT 5;
# ```
#
# This is **very common in analytics**.
#


# ## 🔁 Mental Model
#
# ```text
# FROM table
# → WHERE filter rows
# → ORDER sort
# → LIMIT cut output
# ```

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


#q1
# Write SQL to fetch all rows from sales where price > 20000.
df = pd.read_sql(sql="Select * from sales where price > 20000" , con = conn , index_col= "pid")
print(df)

#q2
# Write SQL to fetch product and quantity where quantity >= 3.
df2 = pd.read_sql(sql="Select product, quantity from sales where quantity > 3" , con = conn)
print(df2)

#q3
# Write SQL to fetch all rows where product = 'Laptop'.
df3 = pd.read_sql(sql="Select * from sales where product = 'Laptop'" , con = conn , index_col= "pid")
print(df3)

#q4
# Write SQL to fetch all rows where:
# price > 10000
# AND quantity >= 2
df4 = pd.read_sql(sql="Select * from sales where price > 10000 AND quantity >= 2" , con = conn , index_col= "pid")
print(df4)

#q5
# Write SQL to fetch all rows where product is either 'Phone' or 'Tablet'.
df5 = pd.read_sql(sql = "Select * from sales where product IN ('Phone' , 'Tablet')" , con = conn)
print(df5)

#q6
# Write SQL to fetch all rows where price is between 5000 and 30000.
df6 = pd.read_sql(sql = "Select * from sales where price BETWEEN  5000 and 30000" , con = conn)
print(df6)

#q7
# Write SQL to fetch:
# product
# price
# from sales
# where product name starts with letter 'S'.

df7 = pd.read_sql("Select product , price from sales where product LIKE 'S%' ", conn)
print(df7)

#q8
# Write SQL to fetch all rows where product name contains the word 'phone'.
df8 = pd.read_sql(sql = "Select * from sales where product IN ('Phone' , 'Tablet')" , con = conn)
print(df8)


#q9
# Write SQL to fetch:
# product
# price
# from sales
# where:
# price > 10000
# product is NOT 'Laptop'
# Order by price descending and limit to 3 rows.

df9 = pd.read_sql(sql = "Select product , price from sales where price > 10000 AND product != 'Laptop'" , con = conn)
print(df9)
