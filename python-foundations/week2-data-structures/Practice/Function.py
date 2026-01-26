
## Default Argument

def printDetails(id , name = "NA", price = "NA"):
    print(f"ID : {id}")
    print(f"Name : {name}")
    print(f"Price: {price}")


# Keyword Argument

def printitem(id , name, price):
    print(f"ID : {id}")
    print(f"Name : {name}")
    print(f"Price: {price}")

#printitem(11559 , "Table" ,1000)


## Variable length Arguments

def sum_1(*elements):   # here *elements make internally an tuple named elements
    res = 0
    for x in elements:
        res = res + x
    return res

#print(sum_1(10 , 20 , 40))

def sum_2(intial , *elements):   # here *elements make internally an tuple named elements
    res = intial
    for x in elements:
        res = res + x
    return res

#print(sum_2(10 , 20 , 40))


## Keyword Length Arguments

def printD(**details): # also possible printD( id , **details) then put  ->printD( 101 , name = "Chips" , price = 100)

    for d,v in details.items():   # here **details is an dictionary so dict.items() make key values in tuple (key , value)
        print(f"{d} is {v}")

#printD(id = 101 , name = "Chips" , price = 100) # here we enter key and value id has key and 101 value both are added in dict details


## Returning Multiple Values in Python

def add_multiply(x ,y):
    sum = x + y
    mul = x * y
    return sum , mul

# s , m = add_multiply(10 , 20)
# print(f"Sum : {s} , Multiplication : {m}" )

def add_multiply_subtract(x ,y):
    sum = x + y
    mul = x * y
    sub = x - y
    return [sum , mul , sub] # Sending as list

s = add_multiply_subtract(10 , 20)   # Even x, y ,z = add_multiply_subtract(10 , 20)  will cause no error as one elemnt of list will beassigned one by one to the variable
#print(s)


## Parameter passing

def fun(x):
    x = 15  # local varaible

x = 10 # Gloabal Variable
fun(x)
#print(x)

def funn(l):
    l.append(15)

l = [10 , 20 , 30]
funn(l)
#print(l)


def f(t):
    t = [40,50]

t = [10 , 20 , 30]
f(t)
#print(t)


# Global Variable

# When a variable is written on left side then python creates local variable ...global can be accessed only on right side ...or for performing any calculation but only right side

def s():
    a = 10 # local variable inside of function
    b = 20 # THeir scope of limit is within the s() function
    print(a, b, c,d)

c = 30
d = 40  # Global Variable  outside of function
#s()
# print(c , d)

# To modify  global variable in an function

def r():
    x = 10
    globals()['x'] = 20    # It is a method to update a global variable in a function
    print(x)

x = 15
# r()
# print(x)


# Lambda Function

# 2️⃣ What IS allowed in lambda
#
#         ✔ Expressions
#         ✔ Conditional expressions
#         ✔ Function calls
#         ✔ Comprehensions (special case)

# 1.Basic Single Argument

# [lambda argument : expression]
square = lambda x: x**2
print(square(5))  # 25

# 2.Multiple Arguments

# [lambda arg1, arg2, arg3 : expression]
calculate_volume = lambda l,w,h : l * w * h
print(calculate_volume(2, 3, 4))  # 24

# 3.Lambda with "If-Else" (Ternary Operator)

# Cant use elif
#lambda x: result_if_true if condition else result_if_false
check_limit = lambda x : "In Limit" if x < 100 else "Out Of Limit"
print(check_limit(150))

# 4.No Arguments

greet = lambda : "Hello World"
print(greet())

# 5.Lambda inside a Dictionary (The "Switch" Trick)

actions = {

    "add" : lambda x,y : x + y,
    "sub" : lambda x,y : x - y,
    "mul" : lambda x,y : x * y
}

print(actions["add"](10,30))
print(actions["sub"](100,30))
print(actions["mul"](10,30))

# 6. Lambda with List Slicing

reverse_str = lambda s : s[::-1]
print(reverse_str("Python"))


# filter, map, and sort   (Works as loops for lambda fuction )

# 1. filter()— The Gatekeeper

#The filter function takes a list and keeps only the items where your condition is True.
#filter(function , list)

nums = [1, 5, 8, 10, 15, 20]

big_nums = list(filter(lambda x: x > 10 , nums))
# print(big_nums)

# 2. map() — The Transformer

#The map function takes a list and applies a change to every single item.

names = ["Yash" , "Arnav" , "Athrava" , "Parth"]

# big_names = list(map(lambda x : x.upper(), names))
# print(big_names)

# 3. sort() and sorted() — The Organizers

# .sort(): Changes the original list (In-place).
#
# sorted(): Returns a new sorted list, leaving the original alone.


words = ["Yash" , "Arnav" , "athrava" , "Soumitra" , "Jay" , "vedant" , "Sahitya" , "parth" , "Abhishek"]

words.sort()  # here 'D' (68) comes before 'b' (98) because 68 is smaller than 98
print(words)

# The Power of the key= argument
# You can tell Python how to look at the data.
# Not Compulsory to use key=

print(sorted(words , key = lambda w : w.lower()))  # Here the sorted() function Alphabetical order is preserved here due to ascii




                                                    # Practice Question


# Find First Digit

# Method 1

def ffd(a):
    while a >= 0:
        a = a // 10
    return a

a = int(input("Enter the number: "))
ans = ffd(a)
print(ans);

# Method 2

import math

def getfirstdigit(a):

    d = int(math.log10(a))    # here log10 of any number give you one less than the actual count of the digits in number
    ans = a // (10**d)
    return ans

# a = int(input("Enter the number: "))
# ans = getfirstdigit(a)
# print(ans)


# Prime Factorization

def prime(x):

    for i in range(2 , int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def pfact(x):

    l = []
    i = 2
    flag = False
    while x > 1:
        if prime(i):
            if x % i == 0:
                x = x // i
                l.append(i)
            else:
                i = i + 1
        else:
            i = i + 1
    return l


# x = int(input("Enter the number: "))
# l = pfact(x)
# print(l)

# Best case method

def prime_factors(n):
    factors = []
    i = 2

    # Check divisors up to √n
    while i * i <= n:      # Here instead of need of to check if number is prime..we take and check weather is it divisible by number till root n as we hav to find factors less than n 0nly
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    # If n is still > 1, it is prime
    if n > 1:
        factors.append(n)

    return factors

# print(prime_factors(100))


# Lambda Question


double_odd = lambda l : [i*2 for i in l if i %2 != 0]
#print(double_odd([10 , 34 , 9 , 7]))
#
# my_list = []
# for i in range(0,10):
#     my_list.append(int(input("Enter values: ")))
#
# print(double_odd(my_list))


#filter, map, and sort question

# Filter: prices = [100, 500, 20, 1500, 300] (Keep only $\ge 100$
# )Map: Apply 10% discount (x * 0.9)
# Sort: Lowest to highest.

prices = [100, 500, 20, 1500, 300]

result = sorted(map(lambda x: x * 0.9, filter(lambda x: x >= 100, prices)))
print(result)


