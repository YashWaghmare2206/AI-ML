
"""
TOPIC 3: POLYMORPHISM & OPERATOR OVERLOADING
--------------------------------------------
Instructions: Complete the following 3 tasks.
"""

# 1. MEDIUM QUESTION: Dynamic Polymorphism (Method Overriding)
# Create a base class 'Shape' with a method 'draw()'.
# Create two child classes 'Circle' and 'Square'.
# Override the 'draw()' method in both child classes to print "Drawing a Circle" and "Drawing a Square".
# Test: Create a list containing a Circle and a Square, loop through it, and call .draw() on both.


# 2. MEDIUM QUESTION: Operator Overloading (The + Symbol)
# Create a class 'Inventory'.
# It should have an attribute 'items' (a list) and 'owner_name'.
# Overload the '__add__' method so that when you use '+' between two Inventory objects:
# - It returns a NEW list containing items from both inventories.
# Test: Create inv1 with ['Sword'] and inv2 with ['Shield']. Print inv1 + inv2.


# 3. HARD QUESTION: Professional Operator Overloading & Logic
# Create a class 'Time' that represents hours and minutes (e.g., 2 hours, 30 minutes).
# Requirements:
# - Use __init__ to store 'hours' and 'minutes'.
# - Overload the '__str__' method to print as "H:MM" (e.g., "2:30").
# - Overload the '__gt__' (Greater Than) method to compare two Time objects.
# - Overload the '__add__' method to add two Time objects.
#   (Note: If minutes exceed 60, increment the hour correctly!)
# Test:
# t1 = Time(1, 45)
# t2 = Time(2, 30)
# print(t1 + t2) # Should output 4:15
# print(t2 > t1) # Should output True


class Shape:

    def draw(self):
        print("Draw Method in Shape")

class Circle(Shape):

    def draw(self):
        print("Drawing a Circle")

class Square(Shape):

    def draw(self):
        print("Drawing a Square")

# s = Shape()
# c = Circle()
# sq = Square()
# l = [s,c,sq]
# for i in l:
#     i.draw()


class Inventory:

    def __init__(self , items , owner_name):
        self.items = items
        self.owner_name = owner_name

    def __add__(self, other):
        return self.items + other.items

    def __str__(self):
        return self.items

inv1 = Inventory(["Sword"], "Vibhuti")
inv2 = Inventory(["Sheild"] , "Manmohan")

# print(inv1 + inv2)


class Time:

    def __init__(self , hr , min):

        if min >= 60:
            self.hr = hr +( min // 60)
            self.min = min % 60
        else:
            self.hr = hr
            self.min = min

    def __str__(self):
        return (f"{self.hr}:{self.min}")

    def __gt__(self, other):

        min1 = self.hr * 60 + self.min
        min2 = other.hr * 60 + other.min

        return True if min1 > min2 else False

    def __add__(self , other):
        return Time(self.hr + other.hr , self.min + other.min)

t1 = Time(1,45)
t2 = Time(2 , 30)

print(t1 + t2)
print(t1 > t2)
