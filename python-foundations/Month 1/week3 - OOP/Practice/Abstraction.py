
"""
TOPIC 4: ABSTRACTION (ABC)
--------------------------
Instructions: Complete these 3 tasks.
"""

# 1. MEDIUM QUESTION: The "Vehicle" Blueprint
# Create an abstract class 'Vehicle' (inheriting from ABC).
# Define an abstract method 'start_engine()'.
# Create two child classes: 'Car' and 'Bike'.
# - Car's start_engine should print "Turning the key..."
# - Bike's start_engine should print "Kicking the starter..."
# Test: Try to create an object of 'Vehicle' (it should fail).
# Then create a Car and Bike and call start_engine().


# 2. MEDIUM QUESTION: Abstract Property Logic
# Create an abstract class 'Employee' with an abstract method 'calculate_salary()'.
# Create a child class 'FullTimeEmployee' with an attribute 'monthly_salary'.
# Create a child class 'Intern' with attributes 'hours_worked' and 'hourly_rate'.
# Implement calculate_salary() in both.
# Test: Create one of each and print their calculated salaries.


# 3. HARD QUESTION: The "Payment Gateway" System
# Create an abstract class 'PaymentProcess'.
# 1. It must have an abstract method 'process_payment(amount)'.
# 2. It must have a NORMAL method 'generate_receipt(amount)' that prints "Receipt for $X generated."
# Create a child class 'PayPal' that implements 'process_payment' by printing "Processing PayPal payment of $X".
# Create a child class 'CreditCard' that implements 'process_payment' by printing "Charging Credit Card $X".
# Test: Use a loop to process a payment of $100 for both PayPal and CreditCard,
# and ensure both also call the generate_receipt() method.


from abc import ABC,abstractmethod



class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        print("Turning the key...")

class Bike(Vehicle):

    def start_engine(self):
        print("Kicking the starter...")

#v = Vehicle()  ## It gives an Error

# c = Car()
# c.start_engine()
# b = Bike()
# b.start_engine()


class Employee:

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self , monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class Intern(Employee):

    def __init__(self , hours_worked , hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

fe = FullTimeEmployee(10000)
i = Intern(1000 , 5)

# print(fe.calculate_salary())
# print(i.calculate_salary())

# 3.

class PaymentProcess:

    @abstractmethod
    def process_payment(self , amount):
        pass

    def generate_receipt(self , amount):
        print(f"Receipt for {amount} generated.")

class PayPal(PaymentProcess):

    def process_payment(self , amount):
        print(f"Processing PayPal payment of {amount}")

class CreditCard(PaymentProcess):

    def process_payment(self , amount):
        print(f"Processing Credit Card  payment of {amount}")

p = PayPal()
c = CreditCard()
for i in range(1,7):
    p.process_payment(200)
    c.process_payment(400)


