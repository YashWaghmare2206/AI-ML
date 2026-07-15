import pandas as pd
import json

# 1️⃣ What is orient?
# orient tells Pandas how JSON data is shaped.
    # Pandas is tabular (rows × columns)
    # JSON is flexible
    # orient is the translation rule


# 2️⃣ The 5 Main orient Types

# a. orient = "records"

# json shape
    # [
    #     { "id": 1, "name": "Asha", "score": 85 },
    #     { "id": 2, "name": "Vikram", "score": 90 }
    # ]

# Read
    # df = pd.read_json("file.json", orient="records")

# Dataframe
#     id    name  score
#     0   1   Asha     85
#     1   2  Vikram    90

# Write
    # df.to_json("out.json", orient="records", indent=4)




# b. orient = "columns"

# json shape
    # {
    #     "id":    { "0": 1, "1": 2 },   it is default but it is called dictionary of lists
    #     "score": { "0": 85, "1": 90 }
    # }

# Read
    # pd.read_json("file.json", orient = "columns")

# ✔️ Default orientation for Pandas
# ❌ Bad for APIs
#❌ Hard for humans



# c. orient = "index"

# json shape
    # {
    #     "row1": { "id": 1, "score": 85 },
    #     "row2": { "id": 2, "score": 90 }
    # }

# Read
    # pd.read_json("file.json", orient="index")

# ✔️ Useful when index is meaningful
# ❌ Rare in APIs


# Feature,                  orient='columns',                   orient='index'
# Top-level Keys,"      Column Names (name, marks)",        "Row Indices (0, 1)"
# Best for...,              Standard data analysis,         Key-value lookups by ID/Index
# File size,                   Usually slightly larger,     Usually slightly smaller


# d. orient="values"

# json shape
    # [
    #     [1, 85],
    #     [2, 90]
    # ]

# Read
    # pd.read_json("file.json", orient="values")

# ⚠️ Loses:
#     Column names
#     Index
# Only use for compact storage.



# e. orient="table" (Schema-based)

# json shape
    # {
    #     "schema": {
    #         "fields": [
    #             {"name": "id", "type": "integer"},
    #             {"name": "score", "type": "integer"}
    #         ],
    #         "primaryKey": ["id"]
    #     },
    #     "data": [
    #         {"id": 1, "score": 85},
    #         {"id": 2, "score": 90}
    #     ]
    # }

# Write
    # df.to_json("file.json", orient="table")

# ✔️ Preserves:
#     dtypes
#     index
#     schema
# ❌ Verbose
# ✔️ Good for data pipelines





# 3️⃣ Quick Comparison Table

# | orient  | Human readable | API friendly | Keeps schema |
# | ------- | -------------- | ------------ | ------------ |
# | records | ✅              | ✅             | ❌            |
# | columns | ❌              | ❌             | ❌            |
# | index   | ⚠️              | ❌             | ❌            |
# | values  | ❌              | ❌             | ❌            |
# | table   | ⚠️              | ⚠️             | ✅            |

# 🧠 Mental shortcut
#
# APIs / sharing → records
#
# Pandas internal → columns
#
# Schema safety → table
#
# Compact → values




# import pandas as pd
#
# df = pd.DataFrame(
#     {
#         "score": [70, 85]
#     },
#     index=["roll1", "roll2"]
# )


# output of file
#         score
# roll1     70
# roll2     85
