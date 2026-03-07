import sqlite3
from SQLite_Basics import *

###  🔹 Topic 2 — Creating Tables in SQLite


#
# This is **foundational**. If tables are wrong, everything breaks later.
#
# ---
#
# ## 1️⃣ What is a Table?
#
# ### Concept
#
# A **table** is:
#
# * Structured storage
# * Made of **rows (records)** and **columns (fields)**
#
# Think of it as:
#
# * CSV with strict rules
# * Each column has a **data type**
#
# ---
#
# ## 2️⃣ CREATE TABLE Syntax
#
# ### General Syntax
#
# ```sql
# CREATE TABLE table_name (
#     column1 datatype,
# column2 datatype,
# column3 datatype
# );
# ```
#
# ---
#
# ### Example
#
# ```sql
# CREATE TABLE sales (
#     id INTEGER,
# product TEXT,
# price REAL,
# quantity INTEGER
# );
# ```
#
# This creates a table named `sales`.
#
# ---
#
# ## 3️⃣ SQLite Data Types (Important but Simple)
#
# SQLite is flexible, but uses these core types:
#
# | Type    | Meaning         | Example     |
# | ------- | --------------- | ----------- |
# | INTEGER | Whole numbers   | 1, 10, 100  |
# | REAL    | Decimal numbers | 10.5, 99.99 |
# | TEXT    | Strings         | 'apple'     |
# | NULL    | Missing value   | None        |
#
# SQLite **does not enforce strict typing**, but we still define them properly.
#
# ---
#
# ## 4️⃣ PRIMARY KEY
#
# ### Concept
#
# * Uniquely identifies each row
# * No duplicates
# * Often used for IDs
#
# ### Example
#
# ```sql
# CREATE TABLE products (
#     id INTEGER PRIMARY KEY,
# name TEXT,
# price REAL
# );
# ```
#
# Now:
#
# * `id` must be unique
# * `id` cannot be NULL
#
# ---
#
# ## 5️⃣ AUTOINCREMENT
#
# ### Concept
#
# * Automatically increases ID
# * You don’t insert it manually
#
# ### Example
#
# ```sql
# CREATE TABLE customers (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# email TEXT
# );
# ```
#
# Now:
#
# ```sql
# INSERT INTO customers (name, email)
# VALUES ('Rahul', 'rahul@gmail.com');
# ```
#
# SQLite auto-fills `id`.
#
# ---
#
# ## 6️⃣ Executing CREATE TABLE from Python
#
# ### Example
#
# ```python
# import sqlite3
#
# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()
#
# cursor.execute("""
#                CREATE TABLE sales (
#                                       id INTEGER PRIMARY KEY,
#                                       product TEXT,
#                                       price REAL,
#                                       quantity INTEGER
#                );
#                """)
#
# conn.commit()
# conn.close()
# ``
# ⚠️ If table already exists → error.
#
#
# ## 7️⃣ Checking Table Schema (Very Useful)
#
# ### Concept
#
# To **see structure of table**:
#
# ```sql
# PRAGMA table_info(table_name);
# ```
#
# ### Example
#
# ```python
# cursor.execute("PRAGMA table_info(sales);")
# print(cursor.fetchall())
# ```
#
# Output meaning:
#`
# (cid, name, type, notnull, default_value, pk)
# ``
#
# ## 8️⃣ DROP TABLE (Danger Zone)
#
# ### Concept
# * Deletes table permanently
# * Data is lost
#
# ### Example
# ```sql
# DROP TABLE sales;
# ```
#
# Use only when needed.
#
# ## 🔁 Safe Version
# ```sql
# DROP TABLE IF EXISTS sales;
# ```
#
# Prevents error if table doesn’t exist.
#
# ## 🔁 Typical Table Design for Data Pipelines
#
# ```sql
# CREATE TABLE cleaned_sales (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
# date TEXT,
# product TEXT,
# price REAL,
# quantity INTEGER,
# revenue REAL
# );

# Used after CSV/JSON cleaning.


## Questions

#q1
# Write SQL to create a table employees with:
# emp_id → auto-increment primary key
# name → text
# salary → real

cursor.execute("""CREATE TABLE employees(emp_id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT , salary REAL);""")
conn.commit()
conn.close()
