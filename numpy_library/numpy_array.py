# 3 main benefits of numpy array over a python list,
# less memory
# fast
# convinient

import numpy as np
import time
import sys

#memory check
a = np.array([1,2,3])
print(a)
print(a[1])

l = range(1000)
print(sys.getsizeof(5) * len(l))

# arange is similar to range
array = np.arange(1000)
print(array.size * array.itemsize)

#numpy array is fast than python list

SIZE = 10000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

#python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("python list took:", (time.time()-start) * 1000)

# numpy array
start = time.time()
result =  a1 + a2
print("numpy took:", (time.time()-start) * 1000)

#convinient
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)