import numpy as np

rng = np.random.default_rng(seed = 1900)

x1 = rng.integers(10 , size = 10)
x2 = rng.integers(10 , size = (3, 3))

# Row 0 → contiguous
# Row 1 → contiguous
# Row 2 → contiguous


print(x1)
print(x2)
## Accessing data

# One Dimensional array
a1 = x1[0 : 3] # slicing as list
a2 = x1[-7]
print(a1)
print(a2)

# Two Dimensional Array
a3 = x2[0 , 2]
print(a3)


# While updating if you inserted an floating point value in the int array then the value will be truncated silently

## Updating a value

# 1D
x1[0 : 4] = 0  # here all elements in the list from index 0 to 3 becomes 0
x1[6] = 0

print(x1)

# 2D
x2[0 , 0] = 1
x2[2 , 2] = 1
print(x2)


