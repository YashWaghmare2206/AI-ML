import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

### 🔹 Topic 1 — SQLite Basics & Setup
#
# I’ll explain **concept → example**, step by step.
# No questions yet (I’ll give them only when you ask).
#
# ---
#
# ## 1️⃣ What is SQLite?
#
# ### Concept
#
# * **SQLite is a lightweight SQL database**
# * It is:
#
# * Serverless ❌ (no MySQL server)
# * File-based ✅
# * Zero configuration ✅
# * Entire database = **one `.db` file**
#
# ### When it’s used
#
# * Data analysis
# * Prototyping pipelines
# * ML feature storage
# * Local projects
# * Small to medium datasets
#
# ### Comparison (quick clarity)
#
# | Database   | Needs Server | Setup     | Best Use              |
# | ---------- | ------------ | --------- | --------------------- |
# | SQLite     | ❌ No         | Very easy | Local data, pipelines |
# | MySQL      | ✅ Yes        | Medium    | Web apps              |
# | PostgreSQL | ✅ Yes        | Harder    | Production analytics  |
#
# ---
#
# ## 2️⃣ SQLite Database File Concept
#
# ### Concept
#
# ```text
# data.db
# ```
#
# * This file **stores everything**:
#
# * Tables
# * Rows
# * Schema
# * Move the file → database moves
# * Delete file → database gone
#
# No cloud. No service. Just a file.
#
# ---
#
# ## 3️⃣ Connecting to SQLite using Python
#
# ### Concept
# To talk to SQLite, Python uses `sqlite3`.
# ### Example
#
# ```python
# import sqlite3
#
# conn = sqlite3.connect('data.db')
# ```
# ### What happens internally
#
# * If `data.db` exists → opens it
# * If not → creates it
# * `conn` = **live connection to DB**
#
# ⚠️ Without connection → no SQL
#
# ## 4️⃣ Connection vs Cursor (Very Important)
#
# ### Concept
# * **Connection (`conn`)**
#
# * Manages the database
# * Commits changes
# * **Cursor (`cursor`)**
#
# * Executes SQL commands
# * Fetches results
#
# Think:
#
# * Connection = phone line 📞
# * Cursor = person talking 🧑
#
# ### Example
#
# ```python
# cursor = conn.cursor()
# ```
#
# Now you can run SQL.

# ## 5️⃣ Executing SQL from Python
#
# ### Concept
#
# * SQL is passed as **string**
# * Cursor executes it
#
# ### Example
#
# ```python
# cursor.execute("SELECT sqlite_version();")
# print(cursor.fetchone())
# ```
#
# ### What this does
#
# * Runs SQL
# * Returns one row
# * `fetchone()` → single row
# * `fetchall()` → all rows
#
# ---
#
# ## 6️⃣ Committing Changes
#
# ### Concept
#
# SQLite does **not save changes automatically**.
#
# If you:
#
# * Create table
# * Insert data
# * Update / Delete
#
# You MUST commit.
#
# ### Example
#
# ```python
# conn.commit()
# ```
# Without commit → changes lost when program ends.
#
# ## 7️⃣ Closing Connection (Good Practice)
#
# ### Example
#
# ```python
# conn.close()
# ```
#
# Why important:
#
# * Frees resources
# * Avoids DB corruption
# * Professional habit
#
# ## 🔁 Minimal Working Template (Remember This)
#
# ```python
# import sqlite3
#
# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()
#
# # SQL here
# cursor.execute("SELECT sqlite_version();")
# print(cursor.fetchone())
#
# conn.commit()
# conn.close()





