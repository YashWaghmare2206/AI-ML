import numpy as np

# --- INITIALIZATION ---
# Setting the seed ensures the "random" numbers are the same every time you run this
rng = np.random.default_rng(seed=1900)

# x1: 1D array with 10 elements
x1 = rng.integers(10, size=10)      # 10 is high only numbers till value 10 will be added
# x2: 2D array (3x3 matrix)
x2 = rng.integers(10, size=(3, 3))

print("Initial x1 (1D):\n", x1)
print("Initial x2 (2D):\n", x2)
print("-" * 30)

# --- 1. RESHAPING ---
# .reshape() changes the structure without changing the data.
# 10 elements can be 2x5, 5x2, or 1x10.
x1_2x5 = x1.reshape((2, 5))
# Using -1 lets NumPy calculate the dimension for you (10 / 5 = 2)
x1_auto = x1.reshape((5, -1))     #The -1 in NumPy's reshape is a placeholder that means "calculate this dimension for me." size = given row X unknow no.o f row(-1)
print("x1 Reshaped to 2x5:\n", x1_2x5)
print("-" * 30)
print("x1 Reshaped to 5x2:\n", x1_auto)
print("-" * 30)

# --- 2. CONCATENATION (Combining) ---
# Create a small 1x3 array to demonstrate stacking with x2
x_extra = np.array([[9, 9, 9]])

print("Before Vertical Stack (x2 + extra row):\n", x2)
print("Before Horizontal Stack (x_extra + x2 side-by-side):\n", x_extra)
print("-" * 30)

# np.concatenate: axis=0 is vertical (rows), axis=1 is horizontal (columns)
concat_v = np.concatenate([x2, x_extra], axis=0)

# vstack: Stacks arrays on top of each other (Vertical)
v_stack = np.vstack([x2, x_extra])

# hstack: Stacks arrays side-by-side (Horizontal)
# Note: x2 is 3x3, so we stack it with itself to keep dimensions valid
h_stack = np.hstack([x2, x2])



print("Vertical Stack (x2 + extra row):\n", v_stack)
print("Horizontal Stack (x2 + x2 side-by-side):\n", h_stack)
print("-" * 30)

# --- 3. SPLITTING ---
# np.split: Breaks 1D array x1 into 3 parts at indices 3 and 7
# Parts will be: [0:3], [3:7], [7:]
part1, part2, part3 = np.split(x1, [3, 7])

# vsplit: Splits a 2D array vertically (at a specific row)
# Let's split x2 after the 1st row
upper_row, lower_rows = np.vsplit(x2, [1])

# hsplit: Splits a 2D array horizontally (at a specific column)
# Let's split x2 after the 2nd column
left_block, right_column = np.hsplit(x2, [2])

print("Split x1 into 3 parts:", part1, part2, part3)
print("vsplit x2 (Upper Row):\n", upper_row)
print("hsplit x2 (Left 2 Columns):\n", left_block)

# 3️⃣ Concatenation ALWAYS Creates a Copy
# This is very important:
# Unlike slicing and reshaping, concatenation always allocates new memory.

# Why?
# Data from different arrays must be placed contiguously
# No single shared buffer possible

# So concatenation is:
# O(n)
# memory-expensive
# ML implication:
# Avoid concatenating inside training loops