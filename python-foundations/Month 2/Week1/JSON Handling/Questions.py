import json
import pandas as pd

##  Python_json_module

# =====================================================
# 🟡 Medium Question 1 — File + Parameters
# =====================================================
# Tasks:
# 1. Read employee.json using the correct json function
# 2. Add a new key "experience" with value 3
# 3. Save the updated data into updated_employee.json
#    - Indented with 4 spaces
#    - Keys sorted alphabetically
# =====================================================

# Step 1: Read JSON data from file
with open("files/Question/employee.json", "r") as f:
    employee_data = json.load(f)

# Step 2: Add new key to the dictionary
employee_data["experience"] = 3

# Step 3: Write updated data back to a new JSON file
with open("files/Question/updated_employee.json", "w") as f:
    json.dump(employee_data, f, indent=4, sort_keys=True)


# =====================================================
# 🟡 Medium Question 2 — String Handling + Error Safety
# =====================================================
# Tasks:
# 1. Convert JSON string into a Python object
# 2. Print only the score
# 3. Convert Python object back into a JSON string
# 4. Handle invalid JSON without crashing
# =====================================================

response = '{"user_id": 12, "status": "ok", "score": 91}'

try:
    # Step 1: Convert JSON string to Python dictionary
    response_data = json.loads(response)

    # Step 2: Access and print the score
    print("Score:", response_data["score"])

    # Step 3: Convert Python object back to JSON string
    response_json_string = json.dumps(response_data)
    print("JSON String:", response_json_string)

except json.JSONDecodeError:
    # Step 4: Handle invalid JSON safely
    print("Error: Invalid JSON string received.")


# =====================================================
# 🔴 Hard Question — Nested JSON + Real-World Thinking
# =====================================================
# Tasks:
# 1. Load the JSON from api_data.json
# 2. Print the name of users whose math marks are greater than 80
# 3. Add a new key "passed": true only for users
#    whose math and science marks are both >= 80
# 4. Save the modified structure back to result.json
#    - JSON must be valid
#    - Indented for readability
#    - Structure unchanged except for new key
# =====================================================

# Step 1: Load nested JSON data from file
with open("files/Question/api_data.json", "r") as f:
    api_data = json.load(f)

# Step 2 & 3: Process each user
users = api_data["data"]["users"]

for user in users:
    # Print user name if math marks > 80
    if user["marks"]["math"] > 80:
        print(user["name"])

    # Add "passed" key only if both marks are >= 80
    if user["marks"]["math"] >= 80 and user["marks"]["science"] >= 80:
        user["passed"] = True

# Step 4: Write updated data back to JSON file
with open("files/Question/result.json", "w") as f:
    json.dump(api_data, f, indent=4)




###  Json in Pandas

# =====================================================
# 🟡 Medium Question 1 — Flat JSON File
# =====================================================
# You are given a file `scores.json`:
# [
#   { "id": 1, "name": "Asha", "score": 78 },
#   { "id": 2, "name": "Vikram", "score": 88 },
#   { "id": 3, "name": "Neha", "score": 91 }
# ]
#
# Tasks:
# 1. Load this JSON into a Pandas DataFrame
# 2. Print only the rows where score >= 85
# 3. Export the filtered DataFrame to `high_scores.json`
# 4. Exported JSON must be in records orientation and pretty printed
# =====================================================

# Step 1: Read flat JSON into DataFrame
df_scores = pd.read_json("files/Question/scores.json")

# Step 2: Filter rows where score >= 85
high_scores = df_scores[df_scores["score"] >= 85]
print(high_scores)

# Step 3 & 4: Export filtered data to JSON
high_scores.to_json(
    "files/Question/high_score.json",
    orient="records",
    indent=4,
    force_ascii=False
)


# =====================================================
# 🟡 Medium Question 2 — JSON Lines (.jsonl)
# =====================================================
# You are given a file `events.jsonl`:
# {"event_id":101,"type":"login"}
# {"event_id":102,"type":"logout"}
# {"event_id":103,"type":"login"}
#
# Tasks:
# 1. Read this file into Pandas correctly
# 2. Count how many times "login" appears
# 3. Print the count
# =====================================================

# Step 1: Read JSON Lines file (lines=True is mandatory)
df_events = pd.read_json("files/Question/events.jsonl", lines=True)

# Step 2: Count number of "login" events
login_count = df_events[df_events["type"] == "login"].shape[0]

# Step 3: Print the count
print("Login count:", login_count)


# =====================================================
# 🔴 Hard Question — pd.read_json Failure Analysis
# =====================================================
# You are given a file `api_response.json`:
# {
#   "status": "success",
#   "data": {
#     "results": [
#       { "id": 1, "marks": 80 },
#       { "id": 2, "marks": 95 }
#     ]
#   }
# }
#
# Tasks:
# 1. Try loading this file directly using pd.read_json (it fails)
# 2. Explain why it fails (nested structure, not tabular)
# 3. Extract only the "results" part
# 4. Convert it into a DataFrame
# 5. Print the DataFrame
#
# Constraints:
# - Do NOT use pd.json_normalize
# - Use json.load, indexing, and pd.DataFrame only
# =====================================================

# Step 1: Load full JSON using standard json module
with open("files/Question/api_response.json", "r") as f:
    raw_data = json.load(f)

# Step 2: Extract the nested "results" list
results = raw_data["data"]["results"]

# Step 3: Convert list of dictionaries to DataFrame
df_results = pd.DataFrame(results)

# Step 4: Print the DataFrame
print(df_results)





### Json Orient


# =====================================================
# 🟡 Medium Question 1 — Identify the `orient`
# =====================================================
# You are given the JSON file `data1.json`:
#
# [
#   { "id": 1, "score": 80 },
#   { "id": 2, "score": 90 }
# ]
#
# Tasks:
# 1. Identify the correct orient
# 2. Read this JSON into a DataFrame
# 3. Export the DataFrame to `out1.json` using the SAME orient
# 4. Pretty-print the output
# =====================================================

# This JSON is a list of dictionaries
# Therefore, the correct orient is "records"

# Step 1 & 2: Read JSON into DataFrame
df1 = pd.read_json("data1.json", orient="records")

# Step 3 & 4: Export DataFrame using same orient
df1.to_json(
    "out1.json",
    orient="records",
    indent=4
)


# =====================================================
# 🟡 Medium Question 2 — Fix the Orient Mismatch
# =====================================================
# Scenario:
# A DataFrame with columns ["name", "age"] was exported using:
#
# df.to_json("people.json", orient="records")
#
# Later, someone tries to read it using:
#
# pd.read_json("people.json", orient="columns")
#
# Tasks:
# 1. Explain what is wrong
# 2. Write the correct read code
# 3. Explain why the corrected code works
# =====================================================

# Explanation:
# - orient="records" creates a list of row-wise dictionaries
# - orient="columns" expects a dictionary of column-wise data
# - This mismatch causes Pandas to misinterpret the structure

# Correct way to read the JSON
df2 = pd.read_json("people.json", orient="records")

# Why this works:
# - The read orient matches the write orient
# - Pandas correctly maps each dictionary to a row


# =====================================================
# 🔴 Hard Question — Multi-Orient Thinking
# =====================================================
# You have a DataFrame:
#
# | id | score |
# |----|-------|
# | 1  | 85    |
# | 2  | 90    |
#
# Tasks:
# 1. Export this DataFrame using:
#    - orient="records"
#    - orient="values"
# 2. Show the exact JSON structure produced by each
# 3. Explain what information is lost in orient="values"
# 4. Read both JSON files back into DataFrames
# 5. Explain why one DataFrame has column names and the other doesn’t
# =====================================================

# Step 1: Create the DataFrame
df3 = pd.DataFrame({
    "id": [1, 2],
    "score": [85, 90]
})

# Step 2: Export using different orients
df3.to_json("records.json", orient="records", indent=4)
df3.to_json("values.json", orient="values", indent=4)

# Step 3: JSON structures produced
#
# records.json:
# [
#   { "id": 1, "score": 85 },
#   { "id": 2, "score": 90 }
# ]
#
# values.json:
# [
#   [1, 85],
#   [2, 90]
# ]

# Step 4: Read both JSON files back into DataFrames
df_records = pd.read_json("records.json", orient="records")
df_values = pd.read_json("values.json", orient="values")

# Step 5: Explanation
# - records.json retains column names because keys exist
# - values.json loses column names and index
# - Pandas auto-assigns column numbers (0, 1) for values.json




