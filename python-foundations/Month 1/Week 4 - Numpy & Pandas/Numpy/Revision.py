import numpy as np

n1 = np.full(shape = (2,3) , fill_value= 7.5)
print(n1)
n2 = np.arange(10 , 50 , 10)
print(n2)
print(n1.dtype , n2.dtype)
print(n1.nbytes , n2.nbytes)   # size of array in bytes

n3 = np.empty(5)
n3.fill(7)       # it fills the unintialized array to an usable one


# linspace V/S arange (Key difference)

# arange(start, stop, step)
# → accumulates floating-point error
# → may miss or overshoot stop
#
# linspace(start, stop, num)
# → computes values mathematically
# → guarantees exact count & endpoints
#
# 🧠 ML & scientific code always prefers linspace.

# Promotion of datatypes

# int32 + float32 → float64
# bool (lowest) → int → float → complex (highest)
# NumPy promotes to the “higher kind” + higher precision


# Why NumPy indexing is O(1)
# 1️⃣ What O(1) really means here
# O(1) means:
# Access time does not depend on array size
# Whether your array has:
# 10 elements
# 10 million elements
# → accessing one element takes the same time
# address = base_address + (index × itemsize)



# ❌ Q3 — Negative indexing
# Your answer:
#
# don’t know, behaves similar to list
#
# That’s honest 👍
# Here’s the correct explanation:
#
# NumPy converts negative indices using:
# index = length + negative_index

# ⚠️ Q4 — Float assigned to int array
# Your answer:
#
# loss of precision, compiler has nothing to do
#
# ✔️ Directionally right
# ❌ ML implication is backwards
#
# Correct reasoning:
# NumPy prioritizes performance
# No runtime checks
# Fixed dtype → forced cast → truncation
#
# Why dangerous in ML:
# You lose decimals silently
# Predictions, gradients, labels can be corrupted
# Model becomes wrong with no error



# 4️⃣ The Most Dangerous Truth
# Slices Are VIEWS, Not Copies
#
# You explicitly wrote:
#
# “Subarrays as no copy views”
#
# Example from your file:
#
# x2[:2, :2] = [[112, 74],
#               [39, 54]]

# Even storing it in an new array and then modifying still changes the original array
# What happened:
# No new array created
# Original x2 modified in-place
# This is intentional design for performance.

# Proof: Shared Memory
#
# If:
# sub = x2[:2, :2]
# sub[0, 0] = 999
#
# Then:
# x2[0, 0] == 999  # True

# 🧠 Same memory, different “window”.




### Topic 5 ( Reshaping Arrays (Views, Strides & When Copies Happen )

# Reshape returns and View
x = np.arange(10)
print(x)
x2 = x.reshape(2,5)   # here (2,3) is not possible only if we can divide then possible 10 element 5 element each row
print(x2)

x3 = x.reshape(5 , -1) # -1 is placholder it means (total_elements / known no. of rows) here rows = 5 so after calculation then -1 replaced with 2 (5 , 2)
print(x3)

# Here as we slice and store the view and then reshape the stored view then new copy is made
y = x[::2]
y.reshape(5, -1)  # forces a copy

# .resize()

# here reshape() returns view/copy based on the way we use it
# but .resize() modifies original array # it is dangerous rarely used



### TOPIC 6 :  Concatenation & Splitting — Building and Breaking Data


rng = np.random.default_rng(seed = 1600)

a1 = rng.integers(10 , size=(3,3))
a2 = rng.integers(10 , size=(1,3))
a3 = rng.integers(10)
print(a1)
print(a2)

a3 = np.concatenate((a1 , a2) , axis= 0)
print(a3)
print(np.vstack([a1,a2])) # similar to a3


a4 = np.concatenate((a1 , a2.reshape(3,1)) , axis=1)
print(a4)
#print(np.hstack([a1,a2]))  this will cause an error as " a2 " as 1x3 it is it should be 3x1


# | Function | Equivalent            |
# | -------- | --------------------- |
# | `vstack` | `concatenate(axis=0)` |
# | `hstack` | `concatenate(axis=1)` |


# Splitting

y = np.split(a1, [3, 7]) # [x1[:3], x1[3:7], x1[7:]]
print(y) # here split by default split along row axis = 0

y2 = np.vsplit(a1, [1, 2])
print(y2)

y3 = np.hsplit(a1, [1, 2])
print(y3)

# 🧠 Mental Model to Lock In
#
# Concatenate = build new memory
# Split = create windows into existing memory


# split = multiple slices at once
