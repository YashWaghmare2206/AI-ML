
import numpy as np


rng = np.random.default_rng(seed = 1701)    # seed reproduces same sequences of random numbers no matter how much time the scripts run
                                            # the RHS returns an generator object that generates an long sequence of numbers and .integer(high = 10 , size == 1d , 2d) gets number in sequences of that long list..it doent returns list

x1 = rng.integers(10 , size = 5)
x2 = rng.integers(10 , size = (3 , 4))
x3 = rng.integers(10 , size = (3 , 4, 5))

# .integers(): To get whole numbers.
# .random(): To get floats between 0 and 1.
# .normal(): To get bell-curve distributed numbers.
# .choice(): To pick from a list.

# No matter how much time you run the code same sequence of answer you will get

# print(x1)
# print(x2)
# print(x3)

                                                                # Numpy Array Attribute

# .shape (Dimensions)
a1 = x3.shape
print(a1)

# .ndim (Rank ..No of axes)
a2 = x2.ndim
print(a2)

# .dtype (Data type)
a3 = x3.dtype
print(a3)

# .size (Total elements)
a4 = x3.size
print(a4)

# .itemsize (Bytes per element)
a5 = x3.itemsize
print(a5)

# .nbytes (Total memory usage)
a6 = x3.nbytes
print(a6)



