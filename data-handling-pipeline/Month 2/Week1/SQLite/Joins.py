

# # 🔹 Topic 8 — JOINs
#
# If you understand JOINs, you understand **real databases**.
#
# As always:
#
# * minimal theory
# * clear patterns
# * coding questions when **you ask**
#
# ---
#
# ## 1️⃣ Why JOIN exists (1-line intuition)
#
# Data is **split across tables** to avoid duplication.
# JOIN lets you **combine related tables**.
#
# Example:
#
# * `orders` table → order info
# * `customers` table → customer info
# JOIN = bring them together.
#
# ---
#
# ## 2️⃣ Tables we’ll assume (mental model)
#
# ### `sales`
#
# | id | product | quantity |
# | -- | ------- | -------- |
#
# ### `customers`
#
# | id | name |
# | -- | ---- |
#
# ### `orders`
#
# | id | customer_id | amount |
# | -- | ----------- | ------ |
#
# ---
#
# ## 3️⃣ INNER JOIN (Most common)
#
# 👉 Return rows **only when match exists in BOTH tables**
#
# ### Syntax
#
# ```sql
# SELECT columns
# FROM table1
# INNER JOIN table2
# ON table1.col = table2.col;
# ```
#
# ---
#
# ### Example
#
# ```sql id="0ibzch"
# SELECT
# orders.id,
# customers.name,
# orders.amount
# FROM orders
# INNER JOIN customers
# ON orders.customer_id = customers.id;
# ```
#
# Only orders that have a valid customer.
#
# ---
#
# ## 4️⃣ LEFT JOIN (VERY IMPORTANT)
#
# 👉 Return **all rows from LEFT table**, match from right if exists.
#
# ### Example
#
# ```sql id="xyp1f3"
# SELECT
# customers.name,
# orders.amount
# FROM customers
# LEFT JOIN orders
# ON customers.id = orders.customer_id;
# ```
#
# Even customers with **no orders** appear (amount = NULL).
#
# ---
#
# ## 5️⃣ RIGHT JOIN (SQLite note ⚠️)
#
# SQLite **does NOT support RIGHT JOIN** directly.
#
# ### Workaround
#
# Swap table order and use LEFT JOIN.
#
# ---
#
# ## 6️⃣ JOIN with WHERE
#
# ```sql id="zsv01b"
# SELECT
# customers.name,
# orders.amount
# FROM customers
# LEFT JOIN orders
# ON customers.id = orders.customer_id
# WHERE orders.amount > 10000;
# ```
#
# ⚠️ This turns LEFT JOIN into INNER JOIN
# (important interview trick)
#
# ---
#
# ## 7️⃣ JOIN with GROUP BY
#
# ```sql id="ej3m4t"
# SELECT
# customers.name,
# SUM(orders.amount) AS total_spent
# FROM customers
# LEFT JOIN orders
# ON customers.id = orders.customer_id
# GROUP BY customers.name;
# ```
#
# Real-world analytics.
#
# ---
#
# ## 8️⃣ Column Name Ambiguity
#
# ❌ Wrong:
#
# ```sql
# SELECT id FROM customers JOIN orders ON id = customer_id;
# ```
#
# ### ✅ Correct
#
# ```sql id="6snjhp"
# SELECT customers.id
# FROM customers
# JOIN orders
# ON customers.id = orders.customer_id;
# ```
#
# Always **prefix table names**.
#
# ---
#
# ## 9️⃣ Pandas Equivalent (for intuition)
#
# ```python
# pd.merge(orders_df, customers_df, left_on='customer_id', right_on='id', how='inner')
# ```
#
# ---
#
# ## 🔁 JOIN Mental Model
#
# ```text
# LEFT TABLE
# ⬅ match condition ➡
# RIGHT TABLE
# ```

import sqlite3

import pandas as pd

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

# # Customers table
# cursor.execute("""
#                CREATE TABLE customers (
#                                           customer_id INTEGER PRIMARY KEY,
#                                           name TEXT,
#                                           city TEXT
#                );
#                """)
#
# # Orders table
# cursor.execute("""
#                CREATE TABLE orders (
#                                        order_id INTEGER PRIMARY KEY,
#                                        customer_id INTEGER,
#                                        amount REAL,
#                                        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
#                );
#                """)

# # Insert customers
# customers_data = [
#     (1, 'Rahul', 'Mumbai'),
#     (2, 'Amit', 'Delhi'),
#     (3, 'Neha', 'Pune'),
#     (4, 'Sara', 'Bangalore')
# ]
#
# cursor.executemany(
#     "INSERT INTO customers VALUES (?, ?, ?)",
#     customers_data
# )
#
# # Insert orders
# orders_data = [
#     (101, 1, 25000),
#     (102, 1, 12000),
#     (103, 2, 18000),
#     (104, 3, 9000),
#     (105, 1, 25000),
#     (106, 1, 12000),
#     (107, 2, 18000),
#     (108, 3, 9000),
#     (109, 1, 25000),
#     (110, 1, 12000),
#     (111, 2, 18000),
#     (112, 3, 9000)
# ]
#
# cursor.executemany(
#     "INSERT INTO orders VALUES (?, ?, ?)",
#     orders_data
# )
#
# conn.commit()



### Question

#q1
# Write SQL to display:
# customer name
# order amount
# Only for customers who have orders.

df1 = pd.read_sql(sql = "Select c.name,o.amount,c.name , COUNT(*) AS total_orders from customers as c INNER JOIN orders as o ON c.customer_id = o.customer_id GROUP BY c.name " , con = conn)
print(df1)

#q2
# Write SQL to display all customers and their order amounts (NULL if no order).
df2 = pd.read_sql("Select * from customers as c LEFT JOIN orders as o ON c.customer_id = o.customer_id" , con = conn)
print(df2)

#q3
# Write SQL to display:
# customer name
# city
# order amount
df3 = pd.read_sql(sql = "Select c.name,c.city,o.amount from customers as c INNER JOIN orders as o ON c.customer_id = o.customer_id " , con = conn)
print(df3)

#q4
# Write SQL to find:
# customer name
# total amount spent by each customer
df4 = pd.read_sql("Select c.name , SUM(o.amount) from customers as c inner join orders as o on c.customer_id = o.customer_id GROUP BY c.name" , con = conn)
print(df4)

#q5
# Write SQL to find customers who have never placed an order.
df5 = pd.read_sql(sql = "Select c.* from customers as c LEFT JOIN orders as o ON c.customer_id = o.customer_id WHERE o.customer_id IS NULL" , con = conn)
print(df5)

#q6
# Write SQL to find:
# customer name
# number of orders placed
df7 = pd.read_sql(sql = "Select c.name , COUNT(o.order_id) as total_orders from customers as c INNER JOIN orders as o on c.customer_id = o.customer_id GROUP BY c.name" , con = conn)
print(df7)

#q7
# Write SQL to find:
# customer name
# total amount spent
# Only include customers whose total spending > 20000.
df8 = pd.read_sql(sql = "Select c.name , SUM(o.amount) as total_spend from customers as c INNER JOIN orders as o on c.customer_id = o.customer_id GROUP BY c.name HAVING total_spend > 20000" , con = conn)
print(df8)

#q8
# Write SQL to find:
# city
# total revenue generated from that city
df9 = pd.read_sql(sql = "Select c.city , SUM(o.amount) as total_spend from customers as c INNER JOIN orders as o on c.customer_id = o.customer_id GROUP BY c.city" , con = conn)
print(df9)

#q10
# Using Pandas + SQL, load:
# customer name
# total amount spent
# sorted by total amount descending.
df10 = pd.read_sql(sql = "Select c.name , SUM(o.amount) as total_spend from customers as c INNER JOIN orders as o on c.customer_id = o.customer_id GROUP BY c.name order by total_spend DESC " , con = conn)
print(df10)
