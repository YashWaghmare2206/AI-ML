names = ["Yash" , "Aayush" , "Arnav" , "Atharav" , "Jay"]

# [expression for item in iterable if condition]..only " if "  condition
# n = [name.upper() for name in names]
# print(n)
#
# #[value_if_true if condition else value_if_false for item in iterable]..only " else "  condition
#
# nums = [1 , 2 , 3, 4, 5]
#
# type = ["Even" if i % 2 == 0 else "Odd" for i in nums]
# print(type)

                                            # Question


#                       # CHALLENGE 2 (Medium): The Threshold Filter
# # Imagine these are "Probability Scores" from an AI model.
# # 1. Given: scores = [0.12, 0.85, 0.44, 0.92, 0.05, 0.61]
# # 2. Create a list called 'high_confidence' that only keeps scores > 0.5.
# # 3. Create another list called 'labels' where:
# #    - If score > 0.5, label is "Pass"
# #    - Else, label is "Fail"
#
# scores = [0.12, 0.85, 0.44, 0.92, 0.05, 0.61]
#
# high_confidence = [score for score in scores if score > 0.5]
# print(high_confidence)
#
# labels = ["Pass" if score > 0.5 else "Fail" for score in scores]
# print(scores)
# print(labels)


                    # # CHALLENGE 3 (Hard): The Matrix Flattener
# # Image data is often stored in nested lists (pixels).
# # 1. Given: image_pixels = [[255, 255, 0], [128, 0, 128], [0, 0, 0]]
# # 2. Use a nested list comprehension to "flatten" this into one single list of numbers.
# # Expected Result: [255, 255, 0, 128, 0, 128, 0, 0, 0]
#
# image_pixels = [[255, 255, 0], [128, 0, 128], [0, 0, 0]]
#
# # [Action | Outer Loop | Inner Loop]    # syntax kind of for nesting
# r = [pixel for sublist in image_pixels for pixel in sublist]
# print(r)

                    # CHALLENGE 4 (Pro): Dictionary to List
# 1. Given: sensor_data = {"temp": 22, "humidity": 45, "pressure": 1012}
# 2. Create a list of strings that looks like this: ["temp=22", "humidity=45", "pressure=1012"]
# Hint: Use .items() inside your comprehension.

sensor_data = {"temp": 22, "humidity": 45, "pressure": 1012}

# ans = [k + str(v) for k,v in sensor_data.items()] # .items() gives tuples like dict to tuple which contains tuples of key and values  and then we can loop

ans = [f"{k}={v}"for k,v in sensor_data.items()]  #f"text {variable}"
print(ans)


                # Multiple "if" Conditions (Logical AND)

# Find numbers divisible by 2 AND divisible by 5
results = [x for x in range(50) if x % 2 == 0 if x % 5 == 0]
# Result: [0, 10, 20, 30, 40]

# Dictionary Comprehension (Creating a Dict from a List)
# This is actually the "reverse" of a list comprehension. You use curly braces {} and define a key: value pair at the start.

fruits = ["apple", "banana", "cherry"]

# Syntax: {key_expression : value_expression for item in list}
fruit_map = {f: len(f) for f in fruits}
print(fruit_map)
# Output: {'apple': 5, 'banana': 6, 'cherry': 6}