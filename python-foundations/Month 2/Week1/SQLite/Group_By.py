import sqlite3

import pandas as pd

# # 🔹 Topic 7 — GROUP BY
#
# Goal:
#
# > **Aggregate data per category instead of whole table**
#
# Without `GROUP BY`
# ➡️ many rows → **one value**
#
# With `GROUP BY`
# ➡️ many rows → **one value per group**
#
# ---
#
# ## 1️⃣ Why GROUP BY exists (1-line intuition)
#
# If you want:
#
# * total sales **per product**
# * average price **per category**
# * count **per customer**
#
# 👉 you **must** use `GROUP BY`
#
# ---
#
# ## 2️⃣ Basic GROUP BY Syntax
#
# ```sql
# SELECT column, AGG_FUNC(column)
# FROM table
# GROUP BY column;
# ```
#
# ---
#
# ### Example
#
# ```sql
# SELECT product, COUNT(*)
# FROM sales
# GROUP BY product;
# ```
#
# Meaning:
#
# * group rows by `product`
# * count rows in each product group
#
# ---
#
# ## 3️⃣ GROUP BY with SUM (Very Common)
#
# ```sql
# SELECT product, SUM(quantity) AS total_qty
# FROM sales
# GROUP BY product;
# ```
#
# Each product → total quantity sold.
#
# ---
#
# ## 4️⃣ GROUP BY with Multiple Aggregates
#
# ```sql
# SELECT
# product,
# COUNT(*) AS orders,
# SUM(quantity) AS total_qty,
# AVG(price) AS avg_price
# FROM sales
# GROUP BY product;
# ```
#
# This is **real analytics SQL**.
#
# ---
#
# ## 5️⃣ GROUP BY Multiple Columns
#
# ```sql
# SELECT
# product,
# price,
# SUM(quantity) AS total_qty
# FROM sales
# GROUP BY product, price;
# ```
#
# Rule:
#
# > Every non-aggregated column in `SELECT`
# > **must appear in GROUP BY**
#
# ---
#
# ## 6️⃣ HAVING vs WHERE (VERY IMPORTANT)
#
# ### WHERE
#
# * filters **rows**
# * runs **before grouping**
#
# ### HAVING
#
# * filters **groups**
# * runs **after grouping**
#
# ---
#
# ### Example
#
# ```sql
# SELECT product, SUM(quantity) AS total_qty
# FROM sales
# GROUP BY product
# HAVING total_qty > 5;
# ```
#
# ❌ This will NOT work:
#
# ```sql
# WHERE total_qty > 5
# ```
#
# ---
#
# ## 7️⃣ GROUP BY + WHERE + HAVING (Real Pattern)
#
# ```sql
# SELECT product, SUM(quantity) AS total_qty
# FROM sales
# WHERE price > 10000
# GROUP BY product
# HAVING total_qty >= 3
# ORDER BY total_qty DESC;
# ```
#
# Execution order (important):
#
# ```
# FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
# ```
#
# ---
#
# ## 8️⃣ Pandas + GROUP BY SQL
#
# ```python
# df = pd.read_sql(
#     """
#     SELECT product, SUM(quantity) AS total_qty
#     FROM sales
#     GROUP BY product
#     """,
#     conn
# )
# print(df)
# ```
#
# ---
#
# ## 🔁 Mental Model
#
# ```text
# Rows
# → WHERE (filter rows)
# → GROUP BY (make groups)
# → AGGREGATE (SUM / COUNT / AVG)
# → HAVING (filter groups)
# ```

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

#q1
# Write SQL to find total quantity sold per product.
df1 = pd.read_sql(sql = "Select product , SUM(quantity) as total_quantity from sales GROUP BY product" , con = conn)
print(df1)

#q2
# Write SQL to count number of rows per product.
df2 = pd.read_sql(sql = "Select product , COUNT(*) as total_rows from sales GROUP BY product" , con = conn)
print(df2)

#q3
# Write SQL to find average price per product.
df3 = pd.read_sql(sql = "Select product , AVG(price) as avg_price from sales GROUP BY product" , con = conn)
print(df3)

#q4
# Write SQL to display:
# product
# total quantity
# total revenue (price × quantity)
# Group by product.
df4 = pd.read_sql(sql = "Select product , SUM(quantity) as total_quantity, SUM(price * quantity) as total_revenue from sales GROUP BY product" , con = conn)
print(df4)

#q5
# Write SQL to find products where total quantity sold ≥ 3.
# df5 = pd.read_sql(sql = "Select product . SUM(sold) as total_quantity_sold from sales HAVING total_quantity_sold >= 3 GROUP BY product" , con = conn)
# print(df5)

# q6
# Write SQL to find:
# product
# total quantity
# Only for rows where price > 10000
df6 = pd.read_sql(sql = "Select product , SUM(quantity) as total_quantity from sales where price > 10000 GROUP BY product" , con = conn)
print(df6)

#q7
# Write SQL to find:
# product
# total quantity
# Only include products where:
# total quantity ≥ 2
# average price > 15000

df7 = pd.read_sql(sql = "Select product , SUM(quantity) as total_quantity , AVG(price) as avg_price from sales HAVING avg_price > 15000 AND total_quantity >= 2 GROUP BY product" , con = conn)
print(df7)

#q8
# Write SQL to find:
# product
# number of orders
# Sort by number of orders descending.
df8 = pd.read_sql(sql = "Select product , SUM(sold) as no_of_orders from sales Group by product ORDER BY no_of_orders DESC" , con=conn)
print(df8)

#q9
# Using Pandas + SQL, load:
# product
# total revenue
# for top 3 products by revenue.

# df9 = pd.read_sql(sql = "Select product , SUM(price * quantity) as total_revenue from sales GROUP BY product ORDER BY total_revenue LIMIT 3" , con=conn)
# print(df9)