                            ### Question Set 1

# TASK 1: The Cleaner
# Given: data = [10, 20, 10, 30, 40, 10, 50]
# 1. Remove all occurrences of 10.
# 2. Sort the remaining list in descending order.
# 3. Print the final list.


# TASK 2: The Slicer
# Given: numbers = list(range(1, 21))  # [1, 2, 3...20]
# Use slicing to:
# 1. Get all even numbers in reverse: [20, 18, 16...2]
# 2. Get the middle 4 numbers: [9, 10, 11, 12]


# TASK 3: The Comprehension Master
# Given: words = ["apple", "it", "creativity", "sun", "python"]
# In ONE line, create a list of tuples where each tuple is (word, length).
# Only include words that are longer than 3 characters.
# Expected: [("apple", 5), ("creativity", 10), ("python", 6)]

# # TASK 1: The Cleaner
#
# data = [10, 20, 10, 30, 40, 10, 50]
# #1.
# data = [i for i in data if i != 10]
# print(data)
# #2.
# data.sort(reverse = True)
# print(data)


# # TASK 2: The Slicer
#
# numbers = list(range(1, 21))  # [1, 2, 3...20]
# #1.
#
# ans = numbers[-1:-20:-2] # here last index taken is -18 that corresponds to 2
# print(ans)
#
# #2. gENERAL
# ans = numbers[]


# TASK 3: The Comprehension Master
#
# words = ["apple", "it", "creativity", "sun", "python"]
#
# #1.
# ans = [(w,len(w)) for w in words]
# print(ans)
#
# #2.
# ans = [w for w in words if len(w) >= 3]
# print(ans)


                            ### Question Set 2

# # CHALLENGE 1: The Duplicate Finder
# # 1. Given: nums = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]
# # 2. Use a list comprehension to create a list of ONLY the numbers that are duplicates.
# # 3. The result should not have duplicates itself (Hint: use set() or count()).
# # Expected: [1, 2, 5]
#
#
# # CHALLENGE 2: Dictionary Swapper
# # 1. Given: stock = {"Apple": 5, "Banana": 12, "Orange": 8}
# # 2. Use a dictionary comprehension to "swap" keys and values.
# # 3. The values should become the keys, and the names should become the values.
# # Expected: {5: 'Apple', 12: 'Banana', 8: 'Orange'}
#
#
# # CHALLENGE 3: Selective Unpacking
# # 1. Given: record = ("ID_99", "John", "Doe", 25, "Engineer", "New York")
# # 2. Use extended unpacking (*rest) to:
# #    - Store the first item in 'user_id'.
# #    - Store the last item in 'city'.
# #    - Store everything in between in a list called 'personal_info'.
#
#
# # CHALLENGE 1: The Duplicate Finder
#
# #1.
# nums = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]
# ans = [nums[i] for i in range(len(nums)) if nums.count(nums[i]) > 1 and nums.index(nums[i]) == i]
# print(ans) # can also be done using set ans = [i for i in set(nums) if nums.count(i) > 1]
# # nums.index(nums[i]) == i this line does that .index(nums[i]) gives index of first occurence of that number so 2nd occurence index i s different then 1st one
#
# # CHALLENGE 2: Dictionary Swapper
#
# stock = {"Apple": 5, "Banana": 12, "Orange": 8}
#
# #1.
# ans = { stock[i]: i for i in stock}
# print(ans)


# # CHALLENGE 3: Selective Unpacking
# # 1. Given: record = ("ID_99", "John", "Doe", 25, "Engineer", "New York")
# # 2. Use extended unpacking (*rest) to:
# #    - Store the first item in 'user_id'.
# #    - Store the last item in 'city'.
# #    - Store everything in between in a list called 'personal_info'.
#
# record = ("ID_99", "John", "Doe", 25, "Engineer", "New York")
#
# #1.
# user_id = record[0]
# print(user_id)
# last_item = record[len(record) - 1]
# print(last_item)
#
# l = list(record)
# print(l)


                                # Question Set 3

# CHALLENGE 4: The Matrix Transposer
# 1. Given a 3x2 matrix: matrix = [[1, 2], [3, 4], [5, 6]]
# 2. Use a NESTED list comprehension to transpose it into a 2x3 matrix.
# Hint: Your outer loop should go through the range of the inner list length.
# Expected: [[1, 3, 5], [2, 4, 6]]


# CHALLENGE 5: Character Frequency Map
# 1. Given: sentence = "abracadabra"
# 2. In ONE line, create a dictionary where:
#    - Key is the character.
#    - Value is how many times it appears in the string.
# Expected: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}


# CHALLENGE 6: The Graded Nested Filter
# 1. Given: students = [
#       ["Kiran", [80, 90, 85]],
#       ["Amit", [40, 50, 45]],
#       ["Sara", [95, 92, 98]]
#    ]
# 2. Use list comprehension to create a list of names for students who have
#    an AVERAGE grade greater than 70.
# Hint: sum(list) / len(list) calculates average.
# Expected: ["Kiran", "Sara"]


# CHALLENGE 4: The Matrix Transposer

matrix = [[1, 2], [3, 4], [5, 6]]

#1.
ans = [ [matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]
# Here first the " col " loop works then it decides how much time " row " works
print(ans)
# Alternate
matrix = [[1, 2], [3, 4], [5, 6]]

# Outer loop: Iterates over column indices (0, 1)
# Inner loop: Picks the i-th element from every row
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transpose) # [[1, 3, 5], [2, 4, 6]]



# CHALLENGE 5: Character Frequency Map

sentence = "abracadabra"

#1.

dict = {i:sentence.count(i) for i in sentence}
print(dict)


# CHALLENGE 6: The Graded Nested Filter

students = [
      ["Kiran", [80, 90, 85]],
      ["Amit", [40, 50, 45]],
      ["Sara", [95, 92, 98]]
   ]

# 1.

ans = [student[0] for student in students if sum(student[1]) / len(student[1]) > 70]
print(ans)


# Extra
names = ["Alice", "Bob"]
scores = [85, 92]
# needed output : 0: {'name': 'Alice', 'score': 85}, 1: {'name': 'Bob', 'score': 92}}

dict = {i: {"name": names[i],"score": scores[i]}for i in range(len(names))}
print(dict)

#Boss Challenge B: Sub-list Summation Given a list of lists, create a new list containing only the sub-lists whose sum is an even number.
#data = [[1, 2], [3, 4], [5, 5], [10, 2]]
# Expected: [[5, 5], [10, 2]]  (Because 10 and 12 are even)

data = [[1, 2], [3, 4], [5, 5], [10, 2]]

ans = [sub for sub in data if  sum(sub) % 2 == 0]
print(ans)