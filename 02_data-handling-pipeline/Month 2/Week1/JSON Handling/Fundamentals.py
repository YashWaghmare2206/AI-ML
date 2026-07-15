## JSON Fundamentals

#JSON(JavaScript Notation Object) and it is a Language independant

# Python Equivalents
# | JSON         | Python           |
# | ------------ | ---------------- |
# | object       | `dict`           |
# | array        | `list`           |
# | string       | `str`            |
# | number       | `int` / `float`  |
# | true / false | `True` / `False` |
# | null         | `None`           |


## JSON Structure

# Json Object  (Keys are string | Only Double Quotes)
# {
#    "name":"Yash"
#     "age": 21,
#     "is_student": true
# }



# Json Array
# 1. Array
# [
#     10,
#     20,
#     30
# ]

# 2. Array of Objects
# [
#     {"id": 1 , "score": 80},
#     {"id": 2 , "score": 90}
# ]



# Nested JSON (this is messy data ..and needs json_normalize to handle this type of data)

# {
#     "user": {
#         "id": 101,
#         "profile": {
#             "name": "Amit",
#             "skills": ["Python", "SQL", "ML"]
#         }
#     }
# }



# JSON as TEXT

# json_text = '{"name": "Yash", "age": 21}'
# This is not a dict yet , becomes when parsing is done
# Thats why : json.loads() exists  |  pd.read_json() exists




# Common Real World JSON Shapes

# API response style
# {
#     "status": "success",
#     "count": 2,
#     "data": [
#         { "id": 1, "score": 80 },
#         { "id": 2, "score": 90 }
#     ]
# }



# 🔑 Mental Model (IMPORTANT)
#
# Think of JSON as:
# A string that describes dictionaries + lists
#
# Python’s job is:
#
# Read the string
# Convert it into Python objects
# Manipulate it
# Convert it back to JSON if needed
