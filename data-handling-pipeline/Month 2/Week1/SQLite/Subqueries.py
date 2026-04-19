# # 🔹 Topic 9 — Subqueries
#
# Subqueries = **query inside another query**.
# They are used when **one query depends on the result of another**.
#
# I’ll keep this **very practical**, no theory dump.
#
# ---
#
# ## 1️⃣ What is a Subquery? (1-line intuition)
#
# > A subquery produces a result that the **outer query uses**.
#
# Think:
#
# * INNER query → computes something
# * OUTER query → uses it
import sqlite3

import pandas as pd

#
# ## 2️⃣ Subquery in `WHERE` (MOST COMMON)
#
# ### Example: customers who spent more than average spending
#
# ```sql
# SELECT c.name
# FROM customers c
# JOIN orders o
# ON c.customer_id = o.customer_id
# GROUP BY c.name
# HAVING SUM(o.amount) >
# (
#     SELECT AVG(amount)
# FROM orders
# );
# ```
#
# Here:
#
# * Inner query → average order amount
# * Outer query → customers exceeding that
#



#
# ## 3️⃣ Subquery with `IN`
#
# ### Example: customers who have placed at least one order
#
# ```sql
# SELECT name
# FROM customers
# WHERE customer_id IN (
#     SELECT DISTINCT customer_id
# FROM orders
# );
# ```
#
# Inner query returns a **list**, outer query matches against it.
#



#
# ## 4️⃣ Subquery with `NOT IN`
#
# ### Example: customers with **no orders**
#
# ```sql
# SELECT name
# FROM customers
# WHERE customer_id NOT IN (
#     SELECT customer_id
# FROM orders
# );
# ```
#
# ⚠️ Note:
#
# * If subquery returns `NULL`, `NOT IN` can behave unexpectedly
# * JOIN solution is often safer (which you already know)
#



#
# ## 5️⃣ Subquery in `SELECT`
#
# ### Example: total orders per customer (without GROUP BY)
#
# ```sql
# SELECT
# c.name,
# (
#     SELECT COUNT(*)
# FROM orders o
# WHERE o.customer_id = c.customer_id
# ) AS total_orders
# FROM customers c;
# ```
#
# This is called a **correlated subquery**
# (inner query depends on outer query).
#



#
# ## 6️⃣ Subquery in `FROM`
#
# ### Example: revenue per customer, then filter
#
# ```sql
# SELECT *
# FROM (
#     SELECT
# c.name,
# SUM(o.amount) AS total_spent
# FROM customers c
# JOIN orders o
# ON c.customer_id = o.customer_id
# GROUP BY c.name
# ) AS customer_totals
# WHERE total_spent > 20000;
# ```
#
# Think of it as:
#
# > “Create a temporary table, then query it”
#


#
# ## 7️⃣ JOIN vs Subquery (Rule of Thumb)
#
# | Situation                    | Prefer   |
# | ---------------------------- | -------- |
# | Simple relationship          | JOIN     |
# | Filtering based on aggregate | Subquery |
# | Step-by-step logic           | Subquery |
# | Performance-critical         | JOIN     |
#



#
# ## 8️⃣ Pandas + Subquery SQL
#
# ```python
# df = pd.read_sql("""
#                  SELECT name
#                  FROM customers
#                  WHERE customer_id IN (
#                      SELECT customer_id FROM orders
#                  )
#                  """, conn)
# ```
#



#
# ## 🔁 Mental Model
#
# ```text
# Outer Query
# └── uses result of
# └── Inner Query
# ```
#

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

### Questions

#q1
# Write SQL to find names of customers who have placed at least one order
# (use a subquery, NOT JOIN).
df1 = pd.read_sql("Select * from customers as c where customer_id IN (Select DISTINCT customer_id from orders as o)" , conn)
print(df1)

#q2
# Write SQL to find names of customers who have NOT placed any order (use subquery).
df2 = pd.read_sql("Select c.name from customers as c where customer_id NOT IN (Select DISTINCT customer_id from orders as o)" , conn)
print(df2)

#q3
# Write SQL to find orders whose amount is greater than the average order amount.
df3 = pd.read_sql("Select * from orders as o  where o.amount > (Select AVG(amount) from orders)" , conn)
print(df3)

#q4
# Write SQL to find customers whose total spending is greater than the average order amount.
df4 = pd.read_sql("Select * from customers as c  where customer_id IN (Select o.customer_id from orders as o GROUP BY customer_id HAVING SUM(amount) > (Select AVG(amount) from orders))" , conn)
print(df4)
# In above question no need to write SUM(amount) at start as it depends were we need ..like if we want to see in it output then "write with select" or if just needed for calculation then write at last

#q5
# Write SQL to find customers who have placed more than 1 order(use subquery, not GROUP BY in outer query).
df5 = pd.read_sql("Select * from customers WHERE customer_id IN (Select o.customer_id from orders as o GROUP BY customer_id HAVING count(o.order_id) > 1 )",conn)
print(df5)

#q6
# Write SQL to find customers who live in cities where at least one order was placed.
df6 = pd.read_sql("SELECT * FROM customers WHERE city IN ( SELECT DISTINCT c.city FROM customers c JOIN orders o ON c.customer_id = o.customer_id)",conn)
print(df6)

#q7
# Write SQL to display:
# customer name
# total amount spent
# Use a subquery in SELECT (correlated subquery).
df7 = pd.read_sql("Select c.name ,  (Select SUM(amount) from orders as o WHERE o.customer_id = c.customer_id)as total_spend from customers as c " , conn)
print(df7)
# here the inner query kind of runs everytime for an particular customer id .,,like selects 1 customer_id then calculates total amount spent for it and then takes 2nd customer_id

#q8 (Here i dont have total_spent column so used average order amount)
# Write SQL to find customers whose total spending is greater than the average spending of all customers
# (Hint: subquery inside HAVING or FROM).
# df8 = pd.read_sql("Select * from customers as c  where customer_id IN (Select o.customer_id from orders as o GROUP BY customer_id HAVING SUM(amount) > (Select AVG(amount) from orders))" , conn)
# print(df8)

# #q9
# Using Pandas + SQL, load:
# customer name
# total spending
# Only for customers whose total spending > 20000,
# using a subquery in FROM.

df9 = pd.read_sql("Select c.name , (Select o.customer_id from orders as o where o.customer_id = c.customer_id  AND SUM(amount) > 20000) FROM customers as c" , conn)
print(df9)

#
# # Q9 Query (Correct Version)
#
# ```sql
# SELECT *
# FROM (
#     SELECT c.name, SUM(o.amount) AS total_spend
# FROM customers c
# JOIN orders o
# ON c.customer_id = o.customer_id
# GROUP BY c.name
# ) AS customer_totals
# WHERE total_spend > 20000;
# ```
#
# ---
#
# # Step 1 — Inner Query Runs First
#
# The part inside `()` runs **first**.
#
# ```sql
# SELECT c.name, SUM(o.amount) AS total_spend
# FROM customers c
# JOIN orders o
# ON c.customer_id = o.customer_id
# GROUP BY c.name
# ```
#
# This calculates **total spending per customer**.
#
# ---
#
# ## Using your dataset
#
# ### customers
#
# | customer_id | name  | city      |
# | ----------- | ----- | --------- |
# | 1           | Rahul | Mumbai    |
# | 2           | Amit  | Delhi     |
# | 3           | Neha  | Pune      |
# | 4           | Sara  | Bangalore |
#
# ### orders
#
# | order_id | customer_id | amount |
# | -------- | ----------- | ------ |
# | 101      | 1           | 25000  |
# | 102      | 1           | 12000  |
# | 103      | 2           | 18000  |
# | 104      | 3           | 9000   |
#
# ---
#
# ## After JOIN
#
# | name  | amount |
# | ----- | ------ |
# | Rahul | 25000  |
# | Rahul | 12000  |
# | Amit  | 18000  |
# | Neha  | 9000   |
#
# ---
#
# ## After GROUP BY
#
# ```sql
# GROUP BY c.name
# ```
#
# Now totals are calculated.
#
# | name  | total_spend |
# | ----- | ----------- |
# | Rahul | 37000       |
# | Amit  | 18000       |
# | Neha  | 9000        |
#
# This result becomes a **temporary table**.
#
# ---
#
# # Step 2 — Subquery Becomes a Temporary Table
#
# SQL treats it like this:
#
# ```
# customer_totals
# ```
#
# | name  | total_spend |
# | ----- | ----------- |
# | Rahul | 37000       |
# | Amit  | 18000       |
# | Neha  | 9000        |
#
# Sara is not here because she has **no orders**.
#
# ---
#
# # Step 3 — Outer Query Runs
#
# Now the outer query runs:
#
# ```sql
# SELECT *
# FROM customer_totals
# WHERE total_spend > 20000
# ```
#
# ---
#
# ## Filtering
#
# | name  | total_spend |
# | ----- | ----------- |
# | Rahul | 37000       |
#
# ---
#
# # Final Result
#
# | name  | total_spend |
# | ----- | ----------- |
# | Rahul | 37000       |
#
# ---
#
# # Mental Model
#
# Think of it as **two queries executed in order**.
#
# ```
# Step 1 → create temporary table
#
# (name, total_spend)
#
# Step 2 → filter that table
# ```
# # Why Use a Subquery in FROM?
#
# Sometimes you want to:
#
# 1. **Compute complex data first**
# 2. **Then filter or analyze it**
#
# Example pattern:
#
# ```
# Raw Data
# ↓
# Aggregate
# ↓
# Temporary Table
# ↓
# Filter / Order / Join
# ```
#
# ---
#
# # SQL Execution Order for This Query
#
# ```
# JOIN
# → GROUP BY
# → SUM()
# → create subquery table
# → WHERE total_spend > 20000
# → SELECT *
# ```
#
# ---
#
