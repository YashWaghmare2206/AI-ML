
# Decorators

# Functions are Objects:

# Functions can be assigned to variables.
# Functions can be passed as arguments to other functions.
# Functions can be defined inside other functions (Nested functions).

# 1. Basic Syntax and Example
def my_decorator(func):   # here while passing " func " it should not contain " () " then it will become method calling

    def wrapper():
        print("Something happening before the func is called")
        func()
        print("Something happeening after the func is called")
    return wrapper()

@my_decorator    # it is an shortcut to say #say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello")

#my_decorator(say_hello)


## 2 .Arguments Handling

# def log(func):
#
#     def wrapper(*args , **kwargs):
#         print(f"Current the function {func.__name__} is running with arguments {args}")
#         result = func(*args , **kwargs)
#         print(f"Result is {result}")
#         return result
#     return wrapper
#
# @log
# def Sum(a, b):
#     return a + b
#
# Sum(100 , 80)


## 3. Class and Static Method

class Pizza:

    def __init__(self , ingredients):
        self.ingredients = ingredients

    # For Users and it retuen string
    def __str__(self):    # necessary for print(pizza object)              # It returns an string
        return f"A delicious pizza with {', '.join(self.ingredients)}"

    # it prints string
    # Needed for developer when we dont use " __str__" then python uses " __repr__"
    def __repr__(self):            # It is written to clearly represent pizza object print(p1) otherwise it gives gibberish value
        print(f" Pizza:ingredients{self.ingredients}")

    @classmethod
    def margetia(cls):
        return cls(['mozzarella', 'tomatoes']) # Here cls returns class object that is pizza object otherwise we wont know which object it belongs it to so it return entire pizza object

    @staticmethod
    def validate_ingredient(ingredient):
        allowed = ['mozzarella', 'tomatoes', 'pepperoni']
        return ingredient in allowed

p1 = Pizza("tomatoes")
r = Pizza.validate_ingredient(p1.ingredients)
print(r)

p2 = Pizza.margetia()

print(p2)