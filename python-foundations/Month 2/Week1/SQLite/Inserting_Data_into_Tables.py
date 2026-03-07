import sqlite3
import pandas as pd

# 1️⃣ INSERT INTO — Basic Syntax
# Minimal theory
#
# Used to add rows to a table.
#
# Syntax
# INSERT INTO table_name (col1, col2)
# VALUES (val1, val2);
# Example
# INSERT INTO sales (product, price, quantity)
# VALUES ('Laptop', 60000, 2);
#
# 📌 Column order must match value order.

# 2️⃣ INSERT from Python (Single Row)
# Example

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute("""
               INSERT INTO sales (product, price, quantity)
               VALUES ('Phone', 30000, 1)
               """)


# 3️⃣ Inserting Multiple Rows
# SQL way
# INSERT INTO sales (product, price, quantity)
# VALUES
# ('TV', 45000, 1),
# ('Tablet', 20000, 3),
# ('Headphones', 3000, 5);

# Python way (executemany)
data = [
    ('TV', 45000, 1),
    ('Tablet', 20000, 3),
    ('Headphones', 3000, 5)
]

cursor.executemany(
    "INSERT INTO sales (product, price, quantity) VALUES (?, ?, ?)",
    data
)
# This is much faster for large inserts.


# 4️⃣ Parameterized Queries (VERY IMPORTANT)
#
# Why needed
# Prevents SQL Injection
# Handles strings safely
# Best practice in pipelines
#
# ❌ Wrong way
# cursor.execute(
#     f"INSERT INTO sales VALUES ('{product}', {price}, {qty})"
# )

# ✅ Correct way

cursor.execute(
    "INSERT INTO sales (product, price, quantity) VALUES (?, ?, ?)",
    ('Camera', 50000, 1)
)
# SQLite replaces ? safely.


# 5️⃣ Inserting Pandas DataFrame → SQL (Most Used)
# Example
# import pandas as pd
#
# df = pd.read_csv('cleaned_data.csv')
#
# df.to_sql(
#     'sales',
#     conn,
#     if_exists='append',
#     index=False
# )

# df.to_sql(...): This is the command that translates that Python table into SQL commands and sends them through your conn (connection).
# 'sales': The name of the table in SQLite where the data will go.
# conn: Your active SQLite connection object.
# if_exists='append': This tells Pandas: "If the table already exists, just add these new rows to the bottom."
# index=False: By default, Pandas tries to turn its row numbers (0, 1, 2...) into a separate column in SQL. This turns that off so you only save your actual data columns.

# Important options
# append → add rows
# replace → drop table + recreate
# fail → error if table exists
# 📌 This is how 90% data pipelines insert data
#
# Attribute,                                What it does
#   name,(Required)                       The name of the SQL table.
#   con,(Required)                The connection engine or sqlite3 connection.
#   schema,                    Used for other databases (like PostgreSQL) to specify a schema. Not usually used for SQLite.
#   if_exists,                'fail': Stop if table exists.  'replace': Delete the old table and make a new one.  'append': Add to the existing table.
#   index,                    True (default) or False. Decides if the DataFrame index becomes a column.
#   index_label,              "If index=True, this lets you name that column (e.g., 'row_num')."
#   chunksize,                "If your CSV is massive (1 million rows), setting chunksize=10000 loads it in smaller batches so your computer doesn't crash."
#   dtype,                    "A dictionary to force specific SQL types (e.g., {'price': 'REAL'}).".

# Example

# import pandas as pd
# import sqlite3
# # You need this to specify the SQL types
# from sqlalchemy import Integer, Text, Float
#
# # 1. Your Data
# data = {
#     'emp_id': [101, 102],
#     'name': ['Alice', 'Bob'],
#     'salary': [75000.50, 82000.00]
# }
# df = pd.DataFrame(data)
#
# # 2. Define the exact types for SQL
# column_types = {
#     'emp_id': Integer,
#     'name': Text,
#     'salary': Float  # Maps to REAL in SQLite
# }
#
# # 3. Send to SQL with the dtype override
# df.to_sql(
#     'employees',
#     conn,
#     if_exists='append',
#     index=False,
#     dtype=column_types
# )

# 6️⃣ Verifying Inserted Data (Quick Check)
df_check = pd.read_sql("SELECT * FROM sales LIMIT 5", conn)
print(df_check)

# Example with all attributes used in .read_sql()
#
# import pandas as pd
# import sqlite3
#
# # 1. Setup Connection
# conn = sqlite3.connect('my_store.db')
#
# # 2. Define our target for the query
# min_price = 50.0
#
# # 3. The Power Move: pd.read_sql with all main attributes
# df_all = pd.read_sql(
#     sql="SELECT * FROM sales WHERE price > ?",  # The SQL Query
#     con=conn,                                   # The Connection
#     index_col='id',                             # Set 'id' as the DataFrame index
#     params=[min_price],                         # Safe way to pass variables
#     parse_dates=['sale_date'],                  # Convert text dates to Python Datetime
#     coerce_float=True                           # Ensure price/salary stay as floats
# )
#
# # Check the results
# print(df_all.head())
# print(df_all.info()) # This shows that 'sale_date' is now a datetime64 type


# 7️⃣ Common Insertion Errors (You MUST recognize)
# a) Column count mismatch
# sqlite3.OperationalError: table has 4 columns but 3 values
#
# Cause: missing column or wrong order.
#
# b) Duplicate primary key
# UNIQUE constraint failed: sales.id
#
# Cause: manual ID insert when AUTOINCREMENT exists.
#
# 🔁 Insertion Flow in Real Project
            # CSV / API JSON
                  # ↓
            # Pandas cleaning
                  # ↓
            # df.to_sql()
                  # ↓
            # SQL querying


## Questions

#q1
# Write SQL to insert one row into table sales with:
# product = 'Mouse'
# price = 599
# conn.execute()

cursor.execute(
    "INSERT INTO sales(product, price, quantity) VALUES(?, ?, ?)",
    ('Mouse', 599.0, 5)
)
#q2
# Write Python + SQLite code to insert:
# product = 'Keyboard'
# price = 1299
# quantity = 2
# into table sales

cursor.execute("INSERT INTO sales(product , price , quantity) VALUES(? , ? , ?)", ('Keyboard' , 1299 , 2))

#q3
# Fix the error in this code:
# cursor.execute(
#     "INSERT INTO sales VALUES ('Monitor', 12000)"
# )
cursor.execute(
    "INSERT INTO sales(product , price , quantity)VALUES ('Monitor', 12000 , 5)"
)


#q4
# Insert multiple rows into table sales using executemany():
# product	price	quantity
# Laptop	70000	1
# Phone	35000	2
# Speaker	5000	4

data = [
    ('Laptop' , 70000 , 1),
    ('Phone' , 3500 , 2),
    ('Speaker' , 5000 , 4)
]

df1 = pd.DataFrame(data)

cursor.executemany("INSERT INTO sales(product , price , quantity) VALUES(? , ? , ?)" , data)

conn.commit()


#q5
# Write Python code to:
# Load cleaned_data.csv
# Insert it into SQLite table sales
# Append data without deleting old rows

from sqlalchemy import Integer, Text, Float
#
# df2 = pd.read_csv("cleaned_data.csv" , sep=',')
# print(df2)
# column_types = {"product" : Text , "price": Float , "quantity" : Integer}
#
# df2.to_sql('sales' , conn , index=False , if_exists='append' , dtype=column_types)


#q6
# Why is this code unsafe? Rewrite it correctly.
#
# cursor.execute(
#     f"INSERT INTO sales VALUES ('{product}', {price}, {qty})"
# )
# The above is dangerous :SQL Injection , data type error , Format error


#q7
df2 = pd.read_csv("cleaned_data.csv", sep=',')
print(df2)
column_types = {
    "product": "TEXT",
    "price": "REAL",
    "quantity": "INTEGER"
}
df2.to_sql('sales' , conn , index=False , if_exists='append' , dtype=column_types)


df_check = pd.read_sql(
    sql= "Select Count(*) as total_count from sales",
    con= conn
)
print(df_check)



#q8

product_to_delete = 0
cursor.execute("DELETE FROM sales where quantity = ?", (product_to_delete,)) # needed as sqlite needs tuple

#q9

# Given this table:
# CREATE TABLE orders (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
# customer TEXT,
# amount REAL
# );
# Write Python code to insert 10 rows using a loop and parameterized query.

for i in range(10):

    customer = str(input("Enter the customer name: "))
    amount = float(input("Enter the amount: "))
    data = (customer , amount)
    cursor.execute("INSERT INTO orders(customer , amount) VALUES(? , ?)",data)

