

# Example

#Dynamic Polymorphism
# Method Overriding

class Employee():

    def __init__(self , id ,name):
        self.id = id
        self.name = name

    def printDetails(self):
        print(f"{self.id} | {self.name}")

class SalesEmployee(Employee):

    def __init__(self , id , name ,salary , sales):
        super().__init__(id , name)
        self.salary = salary
        self.sales = sales

    def printDetails(self):
        print(f"{self.salary} | {self.sales} ")


e = Employee(101 , "Sandeep")
se = SalesEmployee(102 , "Yash" , 10000 , 10)

t_list = [e , se]

for i in t_list:
    i.printDetails()



# Static Polymorphism 
# Method Overloading

class AreaCalculator:
    def calculate_area(self, dim1, dim2=None, *args):
        # Case 1: Only 1 argument (Square)
        if dim2 is None:
            print(f"Square Area: {dim1 * dim1}")
            return dim1 * dim1

        # Case 2: No extra args in *args (Rectangle)
        elif not args:
            print(f"Rectangle Area: {dim1 * dim2}")
            return dim1 * dim2

        # Case 3: Using *args for 3 dimensions (Triangle or Volume)
        else:
            # args is a tuple, e.g., (0.5,) if we pass 3 total arguments
            # Let's say if 3 args are passed, we treat it as a Triangle: (base * height * 0.5)
            if len(args) == 1:
                multiplier = args[0]
                result = dim1 * dim2 * multiplier
                print(f"Triangle Area (using {multiplier}): {result}")
                return result

            # If more args are passed, maybe calculate Volume
            else:
                volume = dim1 * dim2 * args[0]
                print(f"Volume of Box: {volume}")
                return volume

# Usage
calc = AreaCalculator()

calc.calculate_area(5)               # 1 arg -> Square
calc.calculate_area(10, 20)          # 2 args -> Rectangle
calc.calculate_area(10, 20, 0.5)     # 3 args -> Triangle (0.5 is passed to *args)






## Method overloading

"""
PYTHON OPERATOR OVERLOADING (DUNDER METHODS)
--------------------------------------------
This guide maps symbols to their internal magic methods.
"""

class OperatorCheatSheet:
    # 1. ARITHMETIC OPERATORS
    def __add__(self, other):      # Symbol: +
        pass
    def __sub__(self, other):      # Symbol: -
        pass
    def __mul__(self, other):      # Symbol: *
        pass
    def __truediv__(self, other):  # Symbol: /
        pass
    def __floordiv__(self, other): # Symbol: //
        pass
    def __mod__(self, other):      # Symbol: %
        pass
    def __pow__(self, other):      # Symbol: **
        pass

    # 2. COMPARISON OPERATORS
    def __eq__(self, other):       # Symbol: ==
        pass
    def __ne__(self, other):       # Symbol: !=
        pass
    def __lt__(self, other):       # Symbol: <
        pass
    def __gt__(self, other):       # Symbol: >
        pass
    def __le__(self, other):       # Symbol: <=
        pass
    def __ge__(self, other):       # Symbol: >=
        pass

    # 3. ASSIGNMENT OPERATORS (In-place)
    def __iadd__(self, other):     # Symbol: +=
        pass
    def __isub__(self, other):     # Symbol: -=
        pass
    def __imul__(self, other):     # Symbol: *=
        pass
    def __itruediv__(self, other): # Symbol: /=
        pass

    # 4. BITWISE OPERATORS
    def __and__(self, other):      # Symbol: &
        pass
    def __or__(self, other):       # Symbol: |
        pass
    def __xor__(self, other):      # Symbol: ^
        pass
    def __invert__(self):          # Symbol: ~ (Unary)
        pass
    def __lshift__(self, other):   # Symbol: <<
        pass
    def __rshift__(self, other):   # Symbol: >>
        pass

    # 5. COLLECTION & CONTAINER OPERATORS
    def __getitem__(self, key):    # Symbol: obj[key]
        pass
    def __setitem__(self, key, v): # Symbol: obj[key] = val
        pass
    def __delitem__(self, key):    # Symbol: del obj[key]
        pass
    def __contains__(self, item):  # Symbol: item in obj
        pass
    def __len__(self):             # Symbol: len(obj)
        pass

    # 6. OTHER SPECIAL SYMBOLS
    def __call__(self, *args):     # Symbol: obj() (Makes object callable)
        pass
    def __str__(self):             # Symbol: print(obj) (User view)
        pass
    def __repr__(self):            # Symbol: repr(obj) (Dev view)
        pass
    def __enter__(self):           # Symbol: with obj as x: (Start)
        pass
    def __exit__(self, *args):     # Symbol: with obj as x: (End)
        pass


    class Product():

        def __init__(self, name , price):
            self.name = name
            self.price = price

        def __mul__(self , other):
            return self.price * other.price
        

    p1 = Product("Game" , 1000)
    p2 = Product("Food" , 500)

    print(p1 * p2)




