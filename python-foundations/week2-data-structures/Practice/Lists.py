
# Definition: A List is an ordered, mutable (changeable) collection of items.


# list = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
#

                        # # 2. Accessing & Slicing
#
# x = list[5]
# y = list[0:6:2]     # Slice list[start : stop : step]
# z = list[-1:-5:-2]  # step is -2 for moving to left
# m = list[::-1]      # Reverse List
#
# print(x)
# print(y)
# print(z)
# print(m)

                                # 3. Ways of Adding

# my_list = [10 , 20 ,30 , 40 ,50 ,60 ,70 ,80 ,90 ,100]
# list =[110 , 120 ,130 , 140 ,150 ,160 ,170 ,180 ,190 ,200]
#
# my_list.append(0)         #.append(item) adds element at end
# print(my_list)
#
# list.insert(0 , 99)  #.insert(index, item)  add element at specific position
# print(list)
#
# print(my_list.extend(list))      #.extend(another_list) the merged list is the my_list
#
# list3 = my_list + list        #list3 = list1 + list2 (Creates a brand new merged list)
# print(list3)



                                    # 4. Ways of Updating

# list = [11 , 12, 13, 14, 15]
#
# list[0] = 10      #my_list[1] = "New Value" (Replaces whatever was at index 1)
#
# list[0:2] = ["A" , "B"]  #my_list[0:2] = ["A", "B"] (Replaces the first two items at once)
#
# print(list)


                                        # 5. Ways of Deletion

# .pop(index): Removes and returns the item at that index. If no index is given, it removes the last one.
#
# .remove(value): Searches for the first occurrence of a specific value and removes it.
#
# del my_list[index]: Deletes the item at that position.
#
# .clear(): Empties the entire list.


                                            # 6. Built in Methods

# # .index(value)
# colors = ["red", "blue", "green", "blue"]
# print(colors.index("blue"))
#
# #.count(value)
# print(colors.count("blue"))
#
# #.sort()
# nums = [5, 2, 9, 1]
# nums.sort() # Result: [1, 2, 5, 9]
# # To sort backwards: nums.sort(reverse=True)
#
# #.reverse()
# names = ["Zoe", "Abby", "Mark"]
# names.reverse() # Result: ["Mark", "Abby", "Zoe"]


#                                    Question Solving

#    Imp

# step = +1  (left ➜ right) if steps are not given


# CHALLENGE 3 (Medium): Slicing & Reversing
# 1. Given: alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# 2. Slice the list to get ['c', 'd', 'e'] and store it in 'middle'.
# 3. Slice the list to get ['h', 'g', 'f'] (Hint: Use a negative step).
# 4. Print the last 3 items using a single slice.

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#
# middle = alphabet[2:5]
# print(middle)
#
# x = alphabet[-1:-4:-1]
# print(x)
#
# y = alphabet[-3:]   #default step is +1
# print(y)


            # CHALLENGE 4 (Medium): The Organizer
# 1. Given: scores = [45, 88, 12, 99, 34, 67]
# 2. Sort the list in ascending order (smallest to largest).
# 3. Pop the highest score and store it in a variable called 'top_score'.
# 4. Insert the value 0 at the very beginning of the list.

# scores = [45, 88, 12, 99, 34, 67]
#
# scores.sort() # it is in-place sorting so we cant store it another list
# print(scores)
#
# top_score = scores.pop()
# print(top_score)
#
# scores.insert(0,0)
# print(scores)

                # CHALLENGE 5 (Hard): Nested List Drill
# 1. Given: matrix = [[1, 2], [3, 4, 5], [6, 7]]
# 2. Access and print the number 4.
# 3. Add the number 100 to the second inner list ([3, 4, 5]).
# 4. Remove the entire last list ([6, 7]) using .pop().

# matrix = [[1, 2], [3, 4, 5], [6, 7]]
#
# x = matrix[1][1]
# print(x)
#
# matrix[1].append(100)
# print(matrix)
#
# matrix.pop(2)   # is no index given for poping then last element is poped


                # CHALLENGE 6 (Hard): The extend vs append Trap
# 1. Create an empty list called 'main_list'.
# 2. Create another list: 'extra = [10, 20]'.
# 3. Use .append(extra) on main_list.
# 4. Use .extend(extra) on main_list.
# 5. Print main_list and explain why its length is 3 and not 4.

main_list = []
extra = [10, 20]

main_list.append(extra)
main_list.extend(extra)
print(main_list)

#.append() says: "Take this object (the whole list) and put it in the next available slot."

#.extend() says: "Open this box, take every item out one by one, and add them to my list."