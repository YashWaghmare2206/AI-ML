

# Definition: A Tuple is an ordered, immutable (unchangeable) sequence of items.
#
# Syntax: Uses parentheses () instead of square brackets [].
#
# The Key Rule: Once a tuple is born, you cannot add, remove, or change its items. This is called Immutability.


# If single element then it should end with an trailing " , "
# my_tuple = ("apple") # this is not an tuple but an string
#tuple = ("bananan", )  #this is an tuple



                    # 3. Accessing & Slicing
# Since tuples are ordered, they use the exact same indexing and slicing rules as lists.
#
# Access: tp[0] (First item), tp[-1] (Last item).
#
# Slicing: tp[1:3] (Returns a new tuple containing those items).


                        # 4. Built-in Methods
# Because tuples cannot be changed, they have very few methods. They only have two:
#
# .count(x): Returns the number of times x appears.
#
# .index(x): Returns the position of the first x found.



                        # 5. Operations (The "Workarounds")
# While you cannot "update" a tuple, you can perform these operations:
#
# Joining: tp3 = tp1 + tp2 (Creates a brand new tuple).
#
# Repeating: tp * 3 (Repeats the items 3 times in a new tuple). also with list
#
# Deleting: You can't delete an item, but you can delete the whole tuple using del tp.


                            # 6. Tuple Unpacking
# This is a "Superpower" of tuples. You can assign the items of a tuple to variables in one line.

# coordinates = (10, 20, 30) # You keep anyhting here
# x, y, z = coordinates
#
# print(x) # 10
# print(y) # 20

                            # 7. When to use a Tuple over a List?
# Safety: Use it for data that should never change (e.g., Days of the week, GPS coordinates).
#
# Speed: Tuples are slightly faster and use less memory than lists.
#
# Dictionary Keys: Because they are immutable, tuples can be used as keys in a dictionary (Lists cannot).