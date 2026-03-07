import sqlite3
import pandas as pd

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

### 🔹 Topic 4 — SELECT Queries (Reading Data)
#
# Goal of this topic:
# Extract exactly the data you want from SQL
# This is the most used SQL skill in analytics, ML, and pipelines.

# 1️⃣ SELECT * — Read Everything
# Concept (minimal)
#
# Reads all columns and rows from a table.
#
# Example
#SQL
# SELECT * FROM sales
# Python
df1 = pd.read_sql("SELECT * FROM sales", conn)
print(df1)


# 2️⃣ Selecting Specific Columns (Very Important)
# Example
# SQL
# SELECT product, price FROM sales;

# Why this matters:
# Faster queries
# Cleaner data
# Less memory usage

# Python
df2 = (pd.read_sql("SELECT product,price FROM sales" , conn))
print(df2)



# 3️⃣ LIMIT — Control Output Size
# Example
# SELECT * FROM sales LIMIT 5;
#
# Equivalent to:
# df.head(5)   # Used .head() to peek and view only some no. of rows in dataframe

df3 = pd.read_sql(sql="SELECT * FROM sales LIMIT 5" , con = conn)
print(df3)
# 📌 Always use LIMIT while exploring data.



# 4️⃣ DISTINCT — Unique Values
# Example
# SELECT DISTINCT product FROM sales;
#
# Returns:
# Each product name only once

df4 = pd.read_sql("Select DISTINCT product,quantity from sales" , conn)
print(df4)


# 5️⃣ ORDER BY — Sorting Data
# Ascending (default)
# SELECT * FROM sales ORDER BY price;
# Descending
# SELECT * FROM sales ORDER BY price DESC;
# Multiple columns
# SELECT * FROM sales
# ORDER BY price DESC, quantity ASC;

df5 = pd.read_sql("SELECT * FROM sales ORDER BY price" , conn)
df6 = pd.read_sql("SELECT * FROM sales ORDER BY price DESC" , conn)
df7 = pd.read_sql("SELECT * FROM sales ORDER BY price DESC , quantity ASC" , conn)
print(df5)
print(df6)
print(df7)



# 6️⃣ Column Aliases (AS)
# Example
# SELECT
# product,
# price * quantity AS total_value
# FROM sales;
#
# Alias = temporary column name in result.


# 7️⃣ SELECT from Python (Best Practice)
# Example
# query = """
#         SELECT product, price, quantity
#         FROM sales
#         ORDER BY price DESC
#             LIMIT 10 \
#         """
#
# df = pd.read_sql(query, conn)
# print(df)
#
# This is how SQL is actually used in projects.




## Question

#q1
# Write SQL to fetch all columns from table sales

df1 = pd.read_sql("Select * from sales" , conn)
print(df1)

#q2
# Write SQL to fetch only product and price from sales.
df2 = pd.read_sql("Select product , price from sales" , conn)
print(df2)

#q3
# Write SQL to display first 5 rows from sales.

df3 = pd.read_sql("Select * from sales LIMIT 5" , conn)
print(df3)

#q4
# Write SQL to fetch distinct product names from sales.

df4 = pd.read_sql("SELECT DISTINCT product from sales" , conn)
print(df4)

#q5
# Write SQL to fetch all rows from sales sorted by price in descending order.
df5 = pd.read_sql("SELECT * FROM sales ORDER BY price DESC", conn)
print(df5)


#q6
# Write SQL to display:
# product
# price
# quantit
# total_value (price × quantity)
# Use column alias.

df6 = pd.read_sql("Select product , price , quantity , price * quantity as total_value from sales" , conn)
print(df6)

#q7
# Write a Python query string to:
# select product, price
# sort by price descending
# limit to top 3 records

df7 = pd.read_sql("Select product , price from sales ORDER BY price DESC LIMIT 3" , conn)
print(df7)

#q8
# select all column
# order by price DESC
# if prices are equal, order by quantity ASC

query = "SELECT * FROM sales ORDER BY price DESC, quantity ASC"
df_sorted = pd.read_sql(query, conn)

# Primary Sort: price DESC (Expensive -> Cheap)
# Tie-Breaker: quantity ASC (Small -> Large)


#q9
# Using Pandas + SQL, load the top 5 most expensive products into a DataFrame.

df9 = pd.read_sql("Select * from sales ORDER BY price DESC LIMIT 5", conn)
print(df9)