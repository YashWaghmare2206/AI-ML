import numpy as np

## Note
# 1. Numpy array can only contain one type of objects in it..if different type existed then python promotes it using its promotion technique
 #   boolean(lowest) -> int -> float -> complex(highest) and the promotion is only done when original value remains intact



                                            ## Creating an ARRAY from List
l = list(range(20))
arr = np.array(l)  # converting list to array
print(type(arr))   # <class 'numpy.ndarray'>


## Creating array with a certian type
a1 = np.array(range(6) , dtype = np.float32) # float 32 first no. of zeros then the number in 8421 bcd
a2 = np.array(range(6 , 12) , dtype= np.int64)
print(a1)
print(a2)

# " + " here no concatation but individual element addition and the size of array should be same
a3 = a1 + a2 # Here promotion happens flaot32 and int64 has int64 has higher precision and the rule says float over int
             #  but here in this case the float32 is smaller than int65 so float32 to float64 and int64 same then result is float64
print(a3)

print((a1.dtype))
print((a2.dtype))
print((a3.dtype))



#Nested lists in multidimensional array
b1 = np.array([range(i , i + 2)  for i in [2,4,6]] , dtype=np.float32) # inner list are treated as rows
print(b1)


                                        ## Creating Arrays from Scratch

# Creating array filled with 0s
c1 = np.zeros(3 , dtype = int)    # np.zeros(no_of_elements , type of elements)
print(c1)

# Creating an " r x c " matrix filled with 1s but also can do it above
d1 = np.ones( (3 , 4) , dtype = float)  # for 8,16,32,64 bit use  " np.float64 "
print(d1)

# Creating an " r x c " matrix of fixed value
e1 = np.full( (3,3) , 3.14)
print(e1)

# Creating array filled with linear sequence like range( start , stop , step)
f1 = np.arange( 0 , 51 , 5)
print(f1)

# Creating an array of "fixed size " evenly spaced between 0 and 1
                                                                # start = 0 and stop = 1
g1 = np.linspace(0 , 1 , 5)                  # step = (stop - start) / (num - 1) here ans is 0.25
                                                            # HERE then it will be 0 , 0.25 , 0.5..1
print(g1)


# dtype = etc is possible in every function of random


# Creating uniformly distributed multidimensional array
h1 = np.random.random((3,3))  # Size is 3x3 and here the interval is (0.0 , 1.0] here it selects randomly any values between 0 and 1 including 0 but not 1
print(h1)  # and dtype OF elements is float64 high precision it is and the each value as " equal chances of being selected"

h2 = np.random.uniform(5, 9 , (3,3))   # it is similar to np.random.random but we decide " low and high "
print(h2)                                           # " equal chance of every number being selected"


# Normal Distribution | Gaussian Distribution | Bell Curve
# 1. The Three Main Arguments
# loc (Mean): This is the "center" or the peak of the bell curve. Most numbers will be close to this value.
#
# scale (Standard Deviation): This controls the "spread." A small scale makes a tall, skinny curve; a large scale makes a wide, flat curve.
#
# size: The shape of the array (e.g., (3, 3) or 100

l1 = np.random.normal( 1 , 2 , (3, 3))  # Here the values are more near the " loc "(mean) = 1 ..but interval is infinities..less but possible to get values even at extreme
print(l1)                                               # HERE the size is optional



# Random int values
# Here it randomly generates integer between the low and high and the " high " is not included

m1 = np.random.randint(4 , 11  , (4,4) , dtype=np.int64)
print(m1)

m2 = np.random.randint(4   , 11)  # size is optional for all above..default is " single element"
print(m2)


# Identity Matrix

I = np.eye(4) # it generates identity matrix of 4x4
print(I)

# Empty array

t1 = np.empty(3)   # Here it generates an empty array and the entries are bits or bytes that the memory loaction contain..after creation it just sits their
print(t1)

