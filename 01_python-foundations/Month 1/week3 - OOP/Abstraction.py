
#* Abstract Class

# 1. We only " declare " methods in python we do not provide " defination " for that method
# 2. We cannot create object for abstract classes
# 3. Every Method in the abstract class should be " defined " in the class that inherits it
# 4. Normal classes are called " Concrete " classes


from abc import ABC, abstractmethod
#
# class Polygon(ABC):
#
#     def __init__(self , color):
#         self.color = color
#
#     def printSides(self):
#         pass
#
# class Triangle(Polygon):
#
#     def __init__(self , color):
#         super().__init__(color)
#
#     def printSides(self):
#         print("Triangle has 3 sides")
#         print(f" Color is {self.color}")
#
# t = Triangle("Red")
# t.printSides()

                                            # Function in Function

# def fun():
#     print("Inside Fun")
#     def fun1():
#         print("Inside fun1")
#     fun1()
#
# fun()




