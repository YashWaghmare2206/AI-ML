import pandas as pd

## Before code, one critical truth:
# pd.read_json() works only when JSON structure matches a table-like shape
# If the structure is too nested → it fails or gives garbage

# 1️⃣ Basic usage (Simple Json_object)
df = pd.read_json("files/Question/students.json")  #✔️ Works because: | Array of objects | Same keys → columns
print(df)

# 2️⃣ Reading JSON from a string
json_text = '[{"id":1,"score":80},{"id":2,"score":90}]'
df1 = pd.read_json(json_text)   # Valid as json_string as simple structure
print(df1)

# 3️⃣ When read_json() FAILS ❌

# Why?
# Top-level object is NOT a list | Pandas doesn’t know what is a row

# {
#     "status": "success",
#     "data": {
#         "users": [
#             { "id": 1, "score": 80 },
#             { "id": 2, "score": 90 }
#         ]
#     }
# }




# 4️⃣ Important pd.read_json() Parameters

# a. orient  (Tells pandas how JSON is structured)

# | orient    | JSON shape    |
# | --------- | ------------- |
# | `records` | list of dicts |
# | `columns` | dict of lists |
# | `index`   | dict of dicts |
# | `values`  | list of lists |
# | `table`   | schema-based  |

# Example : pd.read_json("file.json", orient="records")


# b. lines  (Used for files having single json object on each line and not entirely wrapped in single bracket like .json file  (the file extension is .jsonl))

df2 = pd.read_json("files/Question/candidate.jsonl", lines=True) # ❌ Without lines=True → crash
print(df2)

# 3. pd.read_json("file.json", dtype={"id": int})
# 4 . pd.read_json("file.json", convert_dates=["date"])   # "date" is column name



# 5️⃣ Mental Model (IMPORTANT)

# | Situation                       | Use                     |
# | --------------------            | ----------------------- |
# | Simple flat JSON                | `pd.read_json`          |
# | API / nested JSON               | `json.load` + normalize |
# | Large streaming data (.jsonl)   | `lines=True`            |
# | Config / settings               | `json.load`             |


# Exporting in pandas

# df.to_json(
#     'output_data.json',
#     orient='records',   # Best for most web applications
#     indent=4,           # Makes it readable
#     date_format='iso',  # Standard date strings
#     force_ascii=False   # Keeps symbols and emojis intact
# )