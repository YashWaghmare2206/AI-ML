import numpy as np

rng = np.random.default_rng(seed = 1701)

## Example of Ufuncs
x = rng.integers(10 , size=10)
print(x)
r = x // 2
print(r)


## Returns of the Ufuncs

# 1. Most Functions (Returning a Copy)
# The vast majority of NumPy functions—including the ones you just asked about (concatenate, split, reshape, vstack, hstack, and transpose)—do not modify the actual array.
# The Logic: They look at the original data, perform the math, and return a brand-new array in a different memory location.

x1 = rng.integers(10 , size=(3,3))
x2 = rng.integers(10 , size=(2,3))
x_new = np.concatenate((x1,x2) , axis=0)
print(x_new)       # x1 and x2 are still exactly as they were



# 2. "In-Place" Operations (Modifying the Actual Array)
# Some specific operations change the array itself. You can usually spot these by two signs:
# Augmented Assignment: Operators like +=, -=, or *=.

print(x1)
x1 += 10  # This MODIFIES the actual x1 array. No copy is made.
print(x1)

# Specific Parameters: Some functions have an out= or inplace=True parameter.
np.add(x1, 20, out=x1) # This forces the result back into x1. # It is an wrap function of " + "
print(x1)

# 3. The "View" Exception (The Tricky Part)
# Functions like .reshape() and .T (Transpose) are special.
# How it works: They don't copy the data to a new memory location, but they also don't "change" the original array's structure.
# The "View": They return a new "view" of the same data.
# The Danger: Because the view and the original share the same memory, if you change a value in the reshaped array,
# it will also change in the original array.

x3 = np.array([1, 2, 3, 4])
view = x3.reshape((2, 2))         # This function returns an view which can be stored in an variable..but changes in viw leads to changes in original data
view[0, 0] = 99  # Changing the view...
print(x3)        # ...now x1 is [99, 2, 3, 4]



                                                    ### Categories of Ufuncs

# 1. The Categories: Unary vs. Binary
# Unary ufuncs: Take one input (e.g., f(x)).
# Binary ufuncs: Take two inputs (e.g., f(x, y)).

# ALl OF THEM RETURN AN COPY...DON'T TOUCH THE ORIGINAL DATA

# Category,                 Unary (1 input),                                    Binary (2 inputs)

# Arithmetic,     "np.negative (−x), np.reciprocal (1/x)"    "np.add, np.subtract, np.multiply, np.divide, np.power"
# Absolute,           np.absolute (or np.abs)                                       None
# Trigonometric,    "np.sin, np.cos, np.tan, np.arcsin"                 np.atan2 (takes x and y coordinates)
# Exponents,             "np.exp (ex), np.exp2 (2x)"                                None
# Logs,             "np.log (ln), np.log10, np.log2"                                None


## Arithmetic Ufuncs

# Operator                                            Ufunc                                       Description

#    +,                                              np.add,                              "Addition (e.g., 1+1=2)"
#    -,                                             np.subtract,                          "Subtraction (e.g., 3−2=1)"
#    *,                                             np.multiply,                          "Multiplication (e.g., 2×3=6)"
#   /,                                                np.divide,                            "True division (e.g., 3/2=1.5)"
#   //,                                              np.floor_divide,                       "Floor division (e.g., 3//2=1)"
#   **,                                               np.power,                             "Exponentiation (e.g., 23=8)"
#   %,                                                np.mod,                               "Modulo/Remainder (e.g., 9%4=1)"

# Example
x4 = rng.integers(15 , size=10)
#Raise all elements to their squares
print(x4)
ans = np.power(x4, 2)
print(ans)


## Absolute Value

x5 = rng.integers(-15 ,0 ,  size=15)   #  syntax for negative or normal one rng.integers(low , high , size=)
print(x5)

# We can also use Pythons normal absolute function with numpy arrays
# And Numpy also have built in ABS function

r1 = abs(x5)  # Python's in-built
r2 = np.abs(x5) # Numpy Array's in-built
print(f"{r1} \n" , r2)



                                                ### Trigonometric Function

thetha = np.linspace(5 , 20 , num=10) # Syntax np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None) if endpoint true than " stop " is included whereas retstep is true it returns " step "

# The values are calculated using machine precision so zero is not actually stored as zero

# Function,                                 Ufunc                                               Description

# Sine,                                    np.sin(x),                                   Returns the sine of each element.
# Cosine,                                  np.cos(x),                                    Returns the cosine of each element.
# Tangent,                                  np.tan(x),                                   Returns the tangent of each element.
# Inverse Sine,                            np.arcsin(x),                                 Returns the inverse sine (arcsin) in radians.
# Inverse Cos,                              np.arccos(x),                                Returns the inverse cosine (arccos) in radians.
# Inverse Tan,                             np.arctan(x),                                 Returns the inverse tangent (arctan) in radians.


## Exponents and Logs


# --- 1. SETTING UP DATA ---
# Using integers 1 through 4 for clean exponential results
x = np.array([1, 2, 3, 4], dtype=float)

# Using powers of 2 for clean log2 results
y = np.array([1, 2, 4, 8, 16], dtype=float)

print(f"Original x: {x}")
print(f"Original y (powers of 2): {y}\n")
print("-" * 40)

# --- 2. EXPONENTIAL FUNCTIONS ---
# np.exp(x) -> calculates e^x (e ≈ 2.718)
e_pow = np.exp(x)

# np.exp2(x) -> calculates 2^x (Common in Computer Science/Binary)
two_pow = np.exp2(x)

# np.power(base, x) -> Raises any base to the power of the array
ten_pow = np.power(10, x)

print("Exponential Results:")
print(f"e^x:      {e_pow}")
print(f"2^x:      {two_pow}")
print(f"10^x:     {ten_pow}\n")
print("-" * 40)

# --- 3. LOGARITHMIC FUNCTIONS ---
# np.log(x) -> Natural log (base e)
natural_log = np.log(x)

# np.log2(y) -> Base-2 log (Crucial for Algorithm Complexity O(log n))
base2_log = np.log2(y)

# np.log10(x) -> Base-10 log (Common in Engineering)
base10_log = np.log10(x)

print("Logarithmic Results:")
print(f"ln(x):     {natural_log}")
print(f"log2(y):   {base2_log}")
print(f"log10(x):  {base10_log}\n")
print("-" * 40)

# --- 4. EDGE CASES & SAFETY ---
# Logarithms are undefined for 0 and negative numbers
z = np.array([-1, 0, 1])

# This will trigger a RuntimeWarning but will still run
with np.errstate(divide='ignore', invalid='ignore'):
    log_z = np.log(z)

print("Handling Edge Cases for Log([-1, 0, 1]):")
print(f"Result: {log_z}")
# -1 becomes 'nan' (Not a Number), 0 becomes '-inf' (Negative Infinity)


## Specialized Functions

# It contain many functions for hyperbolic function , bit arithmetic , comparison operation , radian to degree degree to radian , gamma function


## Advanced Ufunc Features

# Specifying Output

# 3.
e1 = np.arange(5) # Fills array with values from 0 to 4
y = np.empty(5) # allocates an new address and marks 5 spaces in the memory allocated

np.multiply(x,10 ,out=y)
print(e1)


# 2.

y = np.zeros(10)
