import json
import pandas as pd

#q1
with open("user.json" , "r") as f:
    data = json.load(f)
#print(data)

#q2
response = '{"id": 5, "status": "active", "score": 88}'
d1 = json.loads(response)
##print(d1["score"])
response_converted = json.dumps(d1)


#q3

employee = {
    "name": "Ravi",
    "age": 30,
    "department": "IT"
}

with open("employee.json" , "w") as f:
    json.dump(employee , f , indent=4 , sort_keys=True)

#q4
d2 = {"city": "मुंबई"}
d2_jsonstring = json.dumps(d2 , ensure_ascii=False) # No human readable False
print(d2_jsonstring)


#q5
text = "{id: 1, score: 90}"

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")


#q6

with open("config.json" , "r") as f:
    d3 = json.load(f)
d3["version"] = "1.0"
with open("updated_config.json" , "w") as f:
    json.dump(d3 , f , indent=4)

#q7
# json.loads() is required because API responses are JSON strings, not Python objects

response = '{"id": 1, "score": 90}'
data = json.loads(response)
print(data["score"])



#q8

df1 = pd.read_json("data.json")
print(df1)

#q9

data2 = {
    "class": "CS",
    "students": [
        { "id": 1, "score": 80 },
        { "id": 2, "score": 90 }
    ]
}
df2 = pd.json_normalize(data2 , record_path= ['students'] , meta = ["class"])
print(df2)


#q10

data3 = {
    "batch": "2025",
    "results": [
        { "roll": 1, "marks": 70 },
        { "roll": 2, "marks": 85 }
    ]
}

df3 = pd.json_normalize(data3 , record_path=["results"] , meta=["batch"])
print(df3)


#q11

data4 = {
    "dept": "IT",
    "employees": [
        {
            "id": 101,
            "projects": [
                { "name": "Alpha", "hours": 120 },
                { "name": "Beta", "hours": 90 }
            ]
        }
    ]
}

df4 = pd.json_normalize(data4 , record_path=["employees" , "projects"] , meta=["dept" , ["employee" , "id"]])  # To acess the "id" need to provide hieracrchy as just "id" search only at top level but id is buried under employee
print(df4)

#q12

with open("api_response.json" , "r") as f:
    data5 = json.load(f)

df5 = pd.json_normalize(data5 , record_path=["data" , "users"])
print(df5)


#q13

data6 = {
    "course": "Math",
    "students": [
        { "id": 1, "score": 88 },
        { "id": 2 }
    ]
}

df6 = pd.json_normalize(data6 , record_path=["students"] , meta=["course" , "teacher"] , errors="ignore")
print(df6)

#q14

data7 = [
    {
        "id": 1,
        "subjects": [
            { "name": "Math", "marks": 80 },
            { "name": "Science", "marks": 90 }
        ]
    }
]

df7 = pd.json_normalize(data7 , record_path=["subjects"])
print(df7)


#q15

data8 = [
    { "id": 1, "score": 80 },
    { "id": 2 }
]

df8 = pd.json_normalize(data)
print(df8)

#q16

data9 = [
    { "id": 1, "score": 75 },
    { "id": 2 }
]

for i in data9:
    print(i.get("score" , 0))


#q17

data10 = {
    "class": "CS",
    "students": [
        { "id": 1, "score": 88 },
        { "id": 2 }
    ]
}

df10 = pd.json_normalize(data10 , record_path=["students"] , meta=["class" , "teacher"] , errors="ignore")
print(df10)

#q18

data11 = {
    "id": 1,
    "subjects": []
}

df11 = pd.json_normalize(data11)
print(df11)
df11["subjects"] = df11["subjects"].explode()
print(df11)


#q19


data12 = [
    { "id": 1, "score": None },
    { "id": 2, "score": 85 }
]

df12 = pd.json_normalize(data12)
print(df12)
df12["score"] = df12["score"].fillna(0)
print(df12)


# q20

data13 = [
    { "id": 1, "score": 90 },
    { "id": 2, "score": "N/A" },
    { "id": 3, "score": 85 }
]

df13 = pd.json_normalize(data13 , errors="ignore")
df13["score"] = pd.to_numeric(df13["score"] , errors="coerce") # coerce states even if cant convert to numeric so no error occurs
print(df13)
print(df13.dtypes)


#q21

data14 = {
    "course": "Math",
    "students": [
        { "id": 1, "marks": "80" },
        { "id": 2 },
        { "id": 3, "marks": "absent" }
    ]
}

df14 = pd.json_normalize(data14 , record_path=["students"] , meta=["course"])
df14["marks"] = df14["marks"].fillna(0)
df14["marks"] = pd.to_numeric(df14["marks"] , errors="coerce")
print(df14)


data15 = [
    {
        "id": 1,
        "courses": [
            { "name": "Math", "marks": 80 },
            { "name": "Science", "marks": 90 }
        ]
    }
]

df15 = pd.json_normalize(data15)
df15_exploded = df15.explode("courses")
print(df15_exploded)

course_df15 = pd.json_normalize(df15_exploded["courses"])
df15_final = df15.drop(columns=["courses"]).join(course_df15)

print(df15_final)












### JSON orient

#  q22

df16 = pd.read_json("data16.json"  , orient= "records")
print(df16)


# q23

df17 = pd.DataFrame({
    "name": ["Asha", "Vikram"],
    "age": [21, 22]
})

df17.to_json("people.json" , orient="records" , indent=4)

df17 = pd.read_json("people.json" , orient = "records")
print(df17)


# q24

df18 = pd.DataFrame({
    "id": [1, 2],
    "score": [88, 92]
})

df18.to_json("df18.json" , orient="table")
df18 = pd.read_json("df18.json" , orient="table")
print(df18)
print(df18.dtypes)

# one left over question on values orient
df19 = pd.DataFrame({
    "id": [1, 2],
    "score": [85, 90]
})

df19.to_json("values.json" , orient="values")
df19 = pd.read_json("values.json" , orient="values")
print(df19)


df20 = pd.DataFrame(
    {
        "score": [70, 85]
    },
    index=["roll1", "roll2"]
)

df20.to_json("index_data.json", orient="index")
df_new = pd.read_json("index_data.json", orient="index")
print(df_new)