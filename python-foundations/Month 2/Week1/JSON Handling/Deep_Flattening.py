import pandas as pd

# explode() + Deep Flattening (Advanced Nested JSON)

# This is what you use when:
#     JSON is nested multiple levels
#     Lists exist inside columns
#     json_normalize alone is not enough


# Imp definition
# 1️⃣ What explode() does? : Turns one list element into one row

# Example

df = pd.DataFrame({
    "id": [1, 2],
    "skills": [["Python", "SQL"], ["Java", "C++"]]
})

df_exploded = df.explode("skills")  # inner list is broken and every element becomes element of the outer list
print(df_exploded)

# ✔️ Row count increases
# ✔️ Index is duplicated (can reset later)

# if a list inside a list inside a lis

# 1st Explode: Opens the big doll to reveal the medium dolls.
# 2nd Explode: Opens the medium dolls to reveal the small dolls.
# 3rd Explode: Finally gives you the actual values.




# 2️⃣  Explode + Normalize combo (REAL-WORLD PATTERN)

data = [
    {
        "id": 1,
        "courses": [
            { "name": "Math", "marks": 80 },
            { "name": "Science", "marks": 90 }
        ]
    }
]

df1 = pd.json_normalize(data) # Normalize once
print(df1)
df1 = df1.explode("courses") # Explode the list

courses_df = pd.json_normalize(df1["courses"])  # Normalize every times makes an new dataframe with new index starting from 0
df1_final = df1.drop(columns=["courses"]).join(courses_df)

print(df1_final)

# When you run df1.explode(), the index for both rows stays 0.
# When you run pd.json_normalize(df1["courses"]), it creates a new DataFrame with a fresh index: 0 and 1.





### 4️⃣ Multi-level nesting example

data3 = {
    "dept": "CS",
    "students": [
        {
            "id": 1,
            "subjects": [
                { "name": "Math", "score": 80 },
                { "name": "Physics", "score": 90 }
            ]
        }
    ]
}

df = pd.json_normalize(data3 , record_path=["students" , "subjects"] , meta = ["dept"])
print(df)



