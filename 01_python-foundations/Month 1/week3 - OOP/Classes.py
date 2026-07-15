
# Any class created without parent automatically becomes the subclass of the Object class

# class Animal:
#     pass
#
# lion = Animal()
# print(type(lion))

# lion is an object created from the Animal class, type(lion) returns the class of the object along with the module name. Since the class is defined in the current script, the module name is __main__.



# Defining a class named Complex
# A class is a blueprint/template used to create objects
class Complex:

    # Constructor method
    # __init__ is called automatically when an object is created
    # 'self' refers to the current object
    # real and img are instance variables (object data)
    def __init__(self, real, img):
        self.real = real   # stores real part of the complex number
        self.img = img     # stores imaginary part of the complex number

    # Instance method to display the complex number
    # 'self' allows access to the object’s data
    def print(self):
        print(f"{self.real}i + {self.img}j")

    # Instance method to add another Complex object
    # 'c' is another object of the same class
    def add(self, c):
        self.real += c.real   # add real parts
        self.img += c.img     # add imaginary parts


# # Creating object c1 of class Complex
# # Object is an instance of a class
# c1 = Complex(10, 20)
# c1.print()
#
# # Creating another object c2
# c2 = Complex(30, 40)
# c2.print()
#
# # Calling add method of c1 and passing c2 as argument
# # This modifies c1's data
# c1.add(c2)
#
# # Printing updated value of c1
# c1.print()


# Defining a class named Employee
# Class attributes are shared by all objects of the class
class Employee:

    # Class attribute (belongs to the class, not to any single object)
    companyName = "CVE"

    # Constructor to initialize object-specific data
    def __init__(self, id):
        self.id = id    # Instance attribute (unique to each object)

    # Instance method to add an attribute to the object
    def fun(self, name):
        self.name = name   # Instance attribute added dynamically


# Creating an object of Employee class
e = Employee(1001)

# Accessing class attribute using object
# Python first looks inside the object, then inside the class
print(e.companyName)

# Calling instance method
e.fun("Yash")
print(e.name)

# Adding a NEW instance attribute outside the class
# This attribute exists ONLY for object 'e'
e.designation = "CEO"
print(e.designation)

# Changing class attribute using the CLASS NAME
# This affects ALL objects that do not have their own copy
Employee.companyName = "GFG"
print(e.companyName)

# Adding a NEW class attribute dynamically using class name
# This becomes available to ALL objects
Employee.officeAddr = "Navi Mumbai"
print(e.officeAddr)

e.companyName = "ABC"       # Changing  class attribute using instance

print(e.companyName)          # ABC (instance attribute)
print(Employee.companyName)   # GFG (class attribute unchanged)

# What happens if we change class attribute using an OBJECT?      ->   Important

# Python does NOT modify the class attribute
# It creates a new instance attribute named companyName inside object e
# This shadows (hides) the class attribute for that object only


## Types of attribute access

# 1. Public attribute → x (accessible everywhere)
class Test:
    def __init__(self):
        self.x = 10   # public attribute

t = Test()

# Accessible inside class ✔
# Accessible outside class ✔
print(t.x)

# x can be accessed from anywhere
# No restriction at all
# Default access level in Python
# ✅ Use when: data is safe to expose

# 2.Protected (suggested) → _x

class Test:
    def __init__(self):
        self._x = 20   # protected attribute (suggestion)

t = Test()
print(t._x)

# _x is NOT truly protected
# Python allows access, but:
# It’s a developer warning
# Means: “Don’t use this outside the class or subclass”

# 3. Private attribute → __x (name mangling)

class Test:
    def __init__(self):
        self.__x = 30   # private attribute

t = Test()

# This will cause an error ❌
# print(t.__x)

# What Python actually does (NAME MANGLING)
# Python renames __x internally as:
# _ClassName__x
# So here it becomes:
# _Test__x

# 4.Getter for private member

class Test:
    def __init__(self):
        self.__x = 40   # private attribute

    # Getter method
    def get_x(self):
        return self.__x

t = Test()
print(t.get_x())



# THe " _x " means x is an protected variable but python does not enforce it you can still use outside


# Abstract Classes


