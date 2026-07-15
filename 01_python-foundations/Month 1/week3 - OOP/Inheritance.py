

# If a child class does not define __init__, Python automatically uses the parent class’s __init__

# Example

# class Person():
#
#     def __init__(self , id , name):
#         self.id = id
#         self.name = name
#
# class Employee(Person):
#
#     def __init__(self , id , name , salary):
#         super().__init__(id , name)
#         self.salary = salary
#
#     def __str__(self):
#         return f"Details of Employee {self.id} | {self.name} | {self.salary}"
#
#     def printDetails(self):
#         print(self.id , end = " | ")
#         print(self.name , end = " | ")
#         print(self.salary)
#
#
# e1 = Employee(100 , "Yash" , 100000)
# ##print(e1)
# e1.printDetails()



## Types of Inheritance

class Person():

    def __init__(self , id , name):
        self.name = name
        self.id = id

    def printDetails(self):
        print(self.id)
        print(self.name)

class Employee(Person):

    def __init__(self , id , name ,salary):
        super().__init__(id , name)
        self.salary = salary

    def printDetails(self):
        super().printDetails()
        print(self.salary)

class SalEmployee(Employee):

    def __init__(self , id , name , salary , marketing):
        super().__init__(id , name , salary)
        self.marketing = marketing

    def printDetails(self):
        super().printDetails()
        print(self.marketing)


s = SalEmployee(101 , "Yash" , 50000 , 1000)

# Method Overriding
s.printDetails()  # It first goes in the SalEmployee class for searching " PrintDetails" then goes to Employee then Goes to its " PrintDetails " and so on to the top class

## 2. Multiple Inheritance

# Parent Class 1
class Printer:
    def print_doc(self):
        print("Printing the document...")

# Parent Class 2
class Scanner:
    def scan_doc(self):
        print("Scanning the document...")

# Child Class inheriting from BOTH Parent 1 and Parent 2
class MultiFunctionPrinter(Printer, Scanner):
    def show_status(self):
        print("I am a 2-in-1 device: Printer and Scanner.")

# Usage
# 1. Create an object of the child class
device = MultiFunctionPrinter()

# 2. Access method from Printer (Parent 1)
device.print_doc()

# 3. Access method from Scanner (Parent 2)
device.scan_doc()

# 4. Access own method
device.show_status()


# Diamond problem due to Multiple inheritance resolution.

# A common question in multiple inheritance is: "What if both parents have a method with the same name?"
# Python solves this using MRO (Method Resolution Order). It follows a specific order (from left to right) to find the method.
# It first searches in class A as it is inherited first and then in 2nd Class

# Example
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

# Inheriting from A first, then B
class C(A, B):
    pass

obj = C()
obj.greet()  # Output: Hello from A


## MRO Way

# Parent class 1
class Father:
    def __init__(self):
        # Attribute that belongs ONLY to Father
        self.father_name = "Ramesh"
        print("Father __init__ executed")

        # Calls the next class in MRO
        super().__init__()


# Parent class 2
class Mother:
    def __init__(self):
        # Attribute that belongs ONLY to Mother
        self.mother_name = "Sita"
        print("Mother __init__ executed")

        # Calls the next class in MRO
        super().__init__()


# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def __init__(self):
        # Attribute that belongs ONLY to Child
        self.child_name = "Yash"
        print("Child __init__ executed")

        # Starts the MRO chain
        super().__init__()

c = Child()
print(Child.mro())
# Child → Father → Mother → object

# super() does NOT mean “call my parent class”.
# super() means “call the NEXT class in the MRO”.



# # ✅ FINAL REFERENCE: Multiple Inheritance with `__init__` (Python)
#
# ### 🎯 Goal
#
# * `Student` → has `sid`, `deptid`
# * `Faculty` → has `eid`, `deptid`
# * `PhDStudent` → is **both** Student & Faculty
# * Avoid runtime errors
# * Respect **MRO**
# * Use **cooperative initialization**
#
# ---
#
# ## 📌 Code (SAVE THIS)
#
# ```python
# # -----------------------------
# # Multiple Inheritance Reference
# # -----------------------------
#
# class Student:
#     def __init__(self, **kwargs):
#         # Student owns 'sid'
#         self.sid = kwargs.pop("sid")
#
#         # 'deptid' is shared → DO NOT pop
#         self.deptid = kwargs.get("deptid")
#
#         # Pass remaining arguments to next class in MRO
#         super().__init__(**kwargs)
#
#     def get_info(self):
#         return f"StudentID:{self.sid} DepartmentID:{self.deptid}"
#
#
# class Faculty:
#     def __init__(self, **kwargs):
#         # Faculty owns 'eid'
#         self.eid = kwargs.pop("eid")
#
#         # 'deptid' is shared → DO NOT pop
#         self.deptid = kwargs.get("deptid")
#
#         # Continue MRO chain
#         super().__init__(**kwargs)
#
#     def get_info(self):
#         return f"EmployeeID:{self.eid} DepartmentID:{self.deptid}"
#
#
# class PhDStudent(Student, Faculty):
#     def __init__(self, sid, eid, deptid):
#         # Start cooperative initialization
#         # Pass ALL values as keyword arguments
#         super().__init__(sid=sid, eid=eid, deptid=deptid)
#
#     def get_info(self):
#         return f"StudentID:{self.sid} EmployeeID:{self.eid}"
# ```
#
# ---
#
# ## 🧠 HOW THIS WORKS (Step-by-Step)
#
# ### 1️⃣ MRO (Method Resolution Order)
#
# ```python
# print(PhDStudent.mro())
# ```
#
# ```
# [PhDStudent, Student, Faculty, object]
# ```
#
# Python will call `__init__` in **this exact order**.
#
# ---
#
# ### 2️⃣ Object creation
#
# ```python
# p = PhDStudent(1, 101, 10)
# ```
#
# ---
#
# ### 3️⃣ Execution flow
#
# #### 🔹 `PhDStudent.__init__`
#
# ```python
# super().__init__(sid=1, eid=101, deptid=10)
# ```
#
# ---
#
# #### 🔹 `Student.__init__`
#
# ```python
# self.sid = 1
# self.deptid = 10
# super().__init__(eid=101, deptid=10)
# ```
#
# ---
#
# #### 🔹 `Faculty.__init__`
#
# ```python
# self.eid = 101
# self.deptid = 10
# super().__init__()
# ```
#
# ---
#
# #### 🔹 `object.__init__`
#
# ✔ Does nothing → chain ends
#
# ---
#
# ## 📦 Final Object State
#
# ```python
# p.sid      # 1
# p.eid      # 101
# p.deptid   # 10
# ```
#
# ✔ Attributes from **both parents**
# ✔ No duplication
# ✔ No missing values
#
# ---
#
# ## 🚨 WHY `pop()` IS CRITICAL
#
# | Argument | Who owns it | Action       |
# | -------- | ----------- | ------------ |
# | `sid`    | Student     | `pop()`      |
# | `eid`    | Faculty     | `pop()`      |
# | `deptid` | Shared      | `get()` only |
#
# ❌ If you `pop()` a shared value → next class crashes
#     ✅ If you `get()` shared value → safe for all
#
# ---
#
# ## 🔑 GOLDEN RULES (WRITE THESE)
#
# 1. `super()` follows **MRO**, not parent hierarchy
# 2. In multiple inheritance, always use `**kwargs`
# 3. Each class:
#
#     * Initializes **only its own attributes**
#     * Calls `super().__init__()`
# 4. Shared attributes → `get()`, not `pop()`
#
# ---
#
# ## 📌 One-line exam / interview answer
#
# > Python multiple inheritance uses MRO and cooperative `__init__` with `super()` and `**kwargs` to ensure all parent constructors run exactly once without conflicts.
#
# ---
#
# If you want next:
#
# * A **diagram version** of this
# * A **wrong version** and why it fails
# * How Django / mixins use this pattern
#
# Just say 👍



