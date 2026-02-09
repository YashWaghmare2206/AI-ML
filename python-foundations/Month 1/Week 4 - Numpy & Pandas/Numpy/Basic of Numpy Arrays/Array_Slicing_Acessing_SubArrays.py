import numpy as np

rng = np.random.default_rng(seed = 1000)

x1 = rng.integers(20 , size=10)
x2 = rng.integers(20 , size = (3,3))
x3 = rng.integers(20 , size = (6,6))


## For accessing sub arrays using slicing
# syntax variable[ start : stop : step] here default values are start = 0 , stop <= array size(no. of cols or no. of rows) , step = 1


# 1D

# a1 = x1[:3] # here it is 0 to 2
# print(a1)
#
# a2 = x1[3:] # index 3 to last
# print(a2)
#
# a3 = x3[3:8] # 3 to 7
# print(a3)
#
# a4 = x1[1::2] # start 1 till end and step 2
# print(a4)
#
# a5 = x1[4 :: -1] # reversed array -1 runs from 4th element
# print(a5)

# 2D

print(x3)

# b1 = x3[ :2 , : 3] #  First 2 rows and 1 column
# print(b1)

# b2 = x3[ :4 , :: 2] # all 6 rows but every 2nd column
# print(b2)
#
# b3 = x3[ ::-1 , :: -1] # every row and column reversed
# print(b3)

# b4 = x3[ : , 0] # only 1st columnn
# print(b4)
#
# b5 = x3[1:2 , :] # 1:2 means 1:1 only 1st row and all columns   # only for row it can also be x3[0]
# print(b5)
#
# b6 = x3[4] # also means x3[ 4:4 , :]
# print(b6)

                                                                    # Subarrays as no copy views

# No copies exact same array changes there can modify original array


# print(x2)
#
c1 = x2[:2 , :2] = [[ 112 , 74] , [39 , 54]]   # here the 2 x 2 of x2 is updated
# print(x2)


                                                                            # Creating Copies

print(x2)

d1 =  x2[:2 , :2].copy()  # We created an copy on which we can work..no changes in original array
print(d1)



