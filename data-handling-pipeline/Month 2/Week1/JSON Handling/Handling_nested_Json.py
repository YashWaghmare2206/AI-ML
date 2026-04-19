import json
import pandas as pd

# 1️⃣ Why pd.read_json() is NOT enough

# Api Response
# {
#     "status": "success",
#     "data": {
#         "users": [
#             {
#                 "id": 1,
#                 "name": "Asha",
#                 "marks": { "math": 78, "science": 85 }
#             },
#             {
#                 "id": 2,
#                 "name": "Vikram",
#                 "marks": { "math": 92, "science": 88 }
#             }
#         ]
#     }
# }

# ❌ pd.read_json() fails
# ❌ Even if it loads, columns are useless
#
# ➡️ Nested dicts & lists break tabular structure




# 2️⃣ What pd.json_normalize() does?

# Flattens nested JSON into a table

# pd.json_normalize(data)
#     Nested keys become column names
#     " . " is used to join levels




# 3️⃣ Example ( Nested Dictionary only )

data = {       # Its just dicts of dicts
    "id": 1,
    "profile": {
        "name": "Asha",
        "age": 21
    }
}

df = pd.json_normalize(data)
print(df)

# Output   ( Dictionary Flattened )
    # id profile.name  profile.age
    # 0   1        Asha           21





# 4️⃣ Normalizing a List of Objects (COMMON CASE)

users = [
    {
        "id": 1,
        "name": "Asha",
        "marks": { "math": 78, "science": 85 }
    },
    {
        "id": 2,
        "name": "Vikram",
        "marks": { "math": 92, "science": 88 }
    }
]

df = pd.json_normalize(users)
print(df)

# Output
    # id   name  marks.math  marks.science
    # 0   1   Asha          78              85
    # 1   2  Vikram          92              88






data = {
    "class": "CS",
    "students": [
        { "id": 1, "score": 80 },
        { "id": 2, "score": 90 }
    ]
}


# 5️⃣ record_path — Flattening Lists inside JSON

df = pd.json_normalize(
    data,
    record_path="students"   # if data is in deep more levels then  record_path=['level_1', 'level_2', 'level_3'],
)
print(df)


# 6️⃣ meta — Bring Parent Data Along

df1 = pd.json_normalize(
    data,
    record_path="students",
    meta=["class"]        # Which parent fields should be copied to each row
)

print(df1)


# Output for " data " if record path is not used

# class                                           students
# 0   CS   [{'id': 1, 'score': 80}, {'id': 2, 'score': 90}]

    # students stays as a list
    # No row expansion




# When to use " json.normalize() "  and when to use " json.normalize() with record_path"

# 1. json.normalize() : The JSON is already a list, or you want to flatten simple hierarchies like info -> name into info.name.
# 2. json,normalize() with record_path : Your JSON contains metadata (like status or count) at the top, and the actual records are inside a specific key.

# 7️⃣ errors="ignore" — Safe Normalization

# ✔️ Missing keys won’t crash code
pd.json_normalize(
    data,
    record_path="students",
    meta=["class", "teacher"],
    errors="ignore"
)





# 8️⃣ max_level — Control Depth

# pd.json_normalize(data, max_level=1)
    # ✔️ Stops flattening after one level
    # ✔️ Useful for very deep JSON

# Example

# {
#     "id": 1,
#     "name": "Asha",
#     "contact": {
#         "home": {
#             "city": "Mumbai",
#             "pincode": 400001
#         },
#         "work": {
#             "city": "Pune",
#             "pincode": 411001
#         }
#     }
# }

# this code
# df = pd.json_normalize(data, max_level=1)

# Resulting Columns:
    # id
    # name
    # contact.home (This column will contain a dictionary: {'city': 'Mumbai', ...})
    # contact.work (This column will contain a dictionary: {'city': 'Pune', ...})


# 🧠 Mental Model (IMPORTANT)

# | Problem               | Tool                 |
# | --------------------- | -------------------- |
# | Nested dict           | `json_normalize`     |
# | List of dicts         | `json_normalize`     |
# | Parent-child relation | `record_path + meta` |
# | Inconsistent keys     | `errors="ignore"`    |


# 🔹 Rule
#
# If the LIST is the TOP-LEVEL data → use json_normalize() only
# If the LIST is INSIDE a KEY → use record_path



