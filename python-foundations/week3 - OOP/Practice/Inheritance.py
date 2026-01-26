

# 1. Medium Question: The "Smart Home" Hierarchy
# Create a parent class Device with brand and status (on/off).
# Create a child class Light that inherits from Device.
# The Light class should have an additional attribute brightness.
# Requirement: Use super().__init__ in the Light class to initialize the brand.
# Test: Create a Light object and print all its details.

class Device:

    def __init__(self , brand , status):
        self.brand = brand
        self.status = status

class Light(Device):

    def __init__(self , brand , status , brightness):
        super().__init__(brand , status)
        self.brightness = brightness

    def __str__(self):
        return (f"{self.brand} | {self.status} | {self.brightness}")

# l = Light("Philips" , "On" ,1000)
# print(l)


class Animal:

    def eat(self):
        print("The animal eats")

class Mammal(Animal):

    def walk(self):
        print("The animal can walk")

class Dog(Mammal):

    def bark(self):
        print("The Dog barks")

# d = Dog()
# d.eat()
# d.walk()
# d.bark()


class Developer:

    def write_code(self):
        print("Developer writes code")

class Manager:

    def manage_team(self):
        print("Manager manages team")

class TeamLead(Developer , Manager):

    def perform_duties(self):
        super().write_code()
        super().manage_team()

t = TeamLead()
print(t.perform_duties())

print(TeamLead.mro())