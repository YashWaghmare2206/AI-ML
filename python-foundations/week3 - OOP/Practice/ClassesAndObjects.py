
# Level _____Syntax_____Access_____Meaning

# Public ->    self.x ->   obj.x ->          Free for all.
#
# Protected -> self._x ->  obj._x ->         "Please don't use this outside the class."
#
# Private ->   self.__x ->  obj._Class__x ->  "I am hiding this via Name Mangling."
#
#
#





# 1. Medium Question: The "Library Book" System
# Create a class called Book.
#
# Requirements:
# It should have instance attributes for title, author, and a private attribute __is_borrowed (set to False by default).
# Create a method borrow_book() that changes __is_borrowed to True and prints a confirmation.
# Create a method return_book() that changes __is_borrowed to False.
# Create a method status() that prints whether the book is currently available or borrowed.

class Book:

    def __init__(self , title , author , __is_borrowed = False):
        self.title = title
        self.author = author
        self.__is_borrowed = __is_borrowed

    def borrow_book(self):
        self.__is_borrowed = True

    def return_book(self):
        self.__is_borrowed = False

    def status(self):

        if(self.__is_borrowed == True):
            print(f"Book is borrowed")
        else:
            print(f"Book is available")

    def __str__(self):
        return(f"{self.title} | {self.author} | {"Borrowed" if self.__is_borrowed == True else "Available"}")


# b = Book("Python Cookbook" , "Brian Jones")
# print(b)
# b.borrow_book()
# print(b)

# 2. Medium Question: The "Company Tracker"
# Create a class called Project.
# Requirements:
# Add a class attribute named total_projects and set it to 0.
# In the __init__ method, every time a new Project object is created, increment total_projects by
# Each project should have an instance attribute project_name.
# Test: Create three different project objects and print Project.total_projects to confirm it shows 3.

class Project:

    total_projects = 0

    def __init__(self, project_name):
        Project.total_projects += 1
        self.name = project_name


# p1 = Project("CVE")
# p2 = Project("Surakhsha")
# p3 = Project("Academic Assitant")
# print(Project.total_projects)

# 3. Hard Question: The "Secure Bank Account"
# Create a class called BankAccount.
# Requirements:
# Initialize with account_holder (public) and __balance (private).
# Create a Getter method for balance.
# Create a Setter method for balance that only allows the update if the new amount is positive.
# Add a method apply_fees() that subtracts a fixed class attribute TRANSACTION_FEE = 5 from the private balance.
# The Twist: Write a line of code outside the class that attempts to change the private balance using Name Mangling (to prove you know how Python renames private variables).


class BankAccount:

    TRANSACTION_FEE = 5
    def __init__(self , account_holder , __balance = 0.0):
        self.account_holder = account_holder
        self.__balance = __balance

    def get_balance(self):
        return self.__balance

    def apply_fees(self):
        self.__balance -= BankAccount.TRANSACTION_FEE


b = BankAccount(12345 , 1000.0)
print(b.get_balance())
b._BankAccount__balance = 5000.0  # It is Name Mangling internally python does this  " _ + ClassName + __ + AttributeName "
b.apply_fees()
print(b.get_balance())

