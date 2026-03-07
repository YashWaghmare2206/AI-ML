#
#
# # 🔹 Topic 10 — UPDATE & DELETE
#
# These commands **change the database**, unlike `SELECT` which only reads data.
#
# There are **two main operations**:
#
# 1️⃣ **UPDATE** → modify existing rows
# 2️⃣ **DELETE** → remove rows
#
# I’ll explain both using the **same dataset** (`customers`, `orders`).
#


#
# # 1️⃣ UPDATE — Modify Existing Data
#
# ### Basic Syntax
#
# ```sql
# UPDATE table_name
# SET column = new_value
# WHERE condition;
# ```
#
# ---
#
# ## Example 1 — Update a Single Customer City
#
# Change Rahul’s city to **Hyderabad**.
#
# ```sql
# UPDATE customers
# SET city = 'Hyderabad'
# WHERE name = 'Rahul';
# ```
#
# ---
#
# ### What Happens
#
# Before:
#
# | customer_id | name  | city   |
# | ----------- | ----- | ------ |
# | 1           | Rahul | Mumbai |
#
# After:
#
# | customer_id | name  | city      |
# | ----------- | ----- | --------- |
# | 1           | Rahul | Hyderabad |
#



#
# ## Example 2 — Update Multiple Rows
#
# Increase order amount by **1000** for all orders.
#
# ```sql
# UPDATE orders
# SET amount = amount + 1000;
# ```
#
# Here we used **existing column values**.
#



#
# ## Example 3 — Update with Condition
#
# Increase order amount by **10% for orders below 10000**.
#
# ```sql
# UPDATE orders
# SET amount = amount * 1.10
# WHERE amount < 10000;
# ```
#
# ---
#
# # ⚠️ Important Rule (Critical)
#
# If you **forget WHERE**, every row updates.
#
# Example:
#
# ```sql
# UPDATE customers
# SET city = 'Delhi';
# ```
#
# Result:
#
# | name  | city  |
# | ----- | ----- |
# | Rahul | Delhi |
# | Amit  | Delhi |
# | Neha  | Delhi |
# | Sara  | Delhi |
#



#
# # 2️⃣ DELETE — Remove Rows
#
# ### Syntax
#
# ```sql
# DELETE FROM table_name
# WHERE condition;
# ```
#



#
# ## Example 1 — Delete One Order
#
# ```sql
# DELETE FROM orders
# WHERE order_id = 104;
# ```
#
# Removes that order completely.
#



#
# ## Example 2 — Delete Multiple Rows
#
# Delete orders with amount < 10000.
#
# ```sql
# DELETE FROM orders
# WHERE amount < 10000;
# ```
#
# ---
#
# # ⚠️ Critical Rule Again
#
# Without `WHERE`, **all rows are deleted**.
#
# ```sql
# DELETE FROM orders;
# ```
#
# Table stays, but **data is gone**.
#
# ---
#
# # Difference: DELETE vs DROP
#
# | Command | What happens         |
# | ------- | -------------------- |
# | DELETE  | removes rows         |
# | DROP    | removes entire table |
#
# Example:
#
# ```sql
# DROP TABLE orders;
# ```
#
# Table structure is gone.
#
# ---
#
# # Safe Practice Pattern (Professionals Use This)
#
# Before deleting:
#
# ```sql
# SELECT * FROM orders
# WHERE amount < 10000;
# ```
#
# Then run:
#
# ```sql
# DELETE FROM orders
# WHERE amount < 10000;
# ```
#
# Always verify first.
#
# ---
#
# # SQLite + Python Example
#
# ```python
# cursor.execute("""
#                UPDATE customers
#                SET city = 'Hyderabad'
#                WHERE name = 'Rahul'
#                """)
#
# conn.commit()
# ```
#
# For delete:
#
# ```python
# cursor.execute("""
#                DELETE FROM orders
#                WHERE amount < 10000
#                """)
#
# conn.commit()
# ```
#
# ---
#
# # Mental Model
#
# ```text
# SELECT → read data
#
# UPDATE → modify rows
#
# DELETE → remove rows
#
# DROP → remove table
# ```
