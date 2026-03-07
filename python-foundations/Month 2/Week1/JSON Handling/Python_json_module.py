import json


# 2. The Four Main Functions (MEMORIZE THIS TABLE)

# | Function       | Direction     | Input  | Output      |
# | -------------- | ------------- | ------ | ----------- |
# | `json.load()`  | JSON → Python | file   | dict / list |
# | `json.loads()` | JSON → Python | string | dict / list |
# | `json.dump()`  | Python → JSON | file   | writes JSON |
# | `json.dumps()` | Python → JSON | string | JSON string |


# 3. json.load() - Reading from a file

with open("files/files_for_explanation/data.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))   # Dict



# 4. json.loads() — Reading from a string
json_text = '{"id": 1, "score": 85}'

data2 = json.loads(json_text)   # Converts to Python # Without loads its just an text

print(data2)
print(type(data2))  # Dict



# 5. json.dump() — Writing to a file

student = {    # A Python Dict
    "id": 101,
    "name": "Amit",
    "passed": True
}

with open("files/files_for_explanation/students.json", "w") as f:
    json.dump(student , f , indent=4)       # Increases readibility



# 6. json.dumps() — Convert to JSON string (useful for APIs , Logging , Sending data over network)

json_string = json.dumps(json_text)
print(json_string)


# 7. Some Important Parameters

# Indent :  json.dumps(student, indent=4)
# sort_keys: json.dumps(student, sort_keys=True)  # It sorts the key based on Alphabetical order
# ensure_ascii :

data3 = {"city": "मुंबई"}
json.dumps(data3 , ensure_ascii=True) # Default : {"city": "\u092e\u0941\u0902\u092c\u0908"}

print(f" If ensure_ascii in default: {data3}")

json.dumps(data, ensure_ascii=False)   # Dumps convert python to json string
print(data3)




# 8. Common Errors & Handling

text = "{name: Yash}"
#json.loads(text)  # Error : json.decoder.JSONDecodeError

try:
    data = json.loads(text)   # Errorhandled here
except json.JSONDecodeError:
    print("Invalid JSON")


# 🔑 Key Takeaways
#
# JSON is text
# load / dump → files
# loads / dumps → strings
# Output is always Python dict or list
# Indentation is for humans, not machines
