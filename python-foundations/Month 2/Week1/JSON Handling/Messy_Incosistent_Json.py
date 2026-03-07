import pandas as pd
import json

# Real APIs are never clean.
# Common problems you WILL see:
#
# Missing keys
# null values
# Empty lists
# Inconsistent structures
# Partial records


# 1️⃣ Missing Keys (MOST COMMON)

# Example
data = [
    { "id": 1, "score": 80 },
    { "id": 2 }
]

# Solution
df = pd.json_normalize(data)

# Output
print(df)
# id  score
# 0   1   80.0
# 1   2    NaN       Pandas uses NaN




# 2️⃣ Safe Access (Python dict)

# Never use on raw JSON
# user["score"]  # ❌ KeyError

# Safe Way                         ✔️ Prevents crashes
# user.get("score", 0)             # ✔️ Used before normalization sometimes







# 3️⃣ errors="ignore" in json_normalize


data2 = {
    "class": "CS",
    "students": [
        { "id": 1, "score": 80 },
        { "id": 2 }
    ]
}

# Here even if teacher doesnt exit the value becomes NaN
pd.json_normalize(
    data2,
    record_path="students",
    meta=["class", "teacher"],
    errors="ignore"            #  This line does it all
)





# 4️⃣ Empty Lists

data3 = {
    "id": 1,
    "subjects": []
}

# Just json_normalize does
df3 = pd.json_normalize(data3)
# id subjects
# 0   1 []

# explodes() output
df3.explode("subjects")
# id subjects
# 0   1 NaN




#  5️⃣ null values

 # { "id": 1, "score": null }   # Here it is "null" value of json

 # In Pandas -> Nan

 # Solution  # Necessary or problem in math operation
# df["score"] = df["score"].fillna(0)   # Here the Nan replaced with int 0





# 6️⃣ Inconsistent Types (Danger Zone)


# [
#     { "id": 1, "score": 80 },
#     { "id": 2, "score": "N/A" }
# ]

# In Pandas : score → object

# Solution
# df["score"] = pd.to_numeric(df["score"], errors="coerce")

# df["score"] = pd.to_numeric(df["score"], errors="coerce")
# df["score"]: The target column you want to fix.
# pd.to_numeric(...): The conversion tool.
# errors="coerce": The most important part. * Normally, if Pandas hits a string like "N/A", it will crash with an error.
# "coerce" tells Pandas: "If you can't turn it into a number, don't crash—just force it to be NaN (null)."
#
#

