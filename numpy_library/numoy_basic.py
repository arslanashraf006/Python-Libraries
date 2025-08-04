import numpy as np

a = np.array([5,6,7])
print(a[1])

a = np.array([[1,2], [3,4], [5,6]])
print(a.ndim) # print dimensions
print(a.itemsize) # byte size
print(a.dtype) # datatype

a = np.array([[1,2], [3,4], [5,6]], dtype=np.float64)
print(a.itemsize)
print(a)
print(a.size) # total elements
print(a.shape) # rows and column

a = np.array([[1,2], [3,4], [5,6]], dtype=complex)
print(a)

# array with all zeros
print("array with zeros:", np.zeros((3,4)))
#array wit all ones
print("array with ones:", np.ones((3,4)))

print("arange:", np.arange(1,5))
print("arange with steps:", np.arange(1,5,2)) # start, end, steps

print("linearly spaced numbers:",np.linspace(1,5,10))#it will geneated 10 numbers b/w 1 and 5 which are linearly spaced

#reshape
a = np.array([[1,2], [3,4], [5,6]])
print(a.shape)
print("reshape:", a.reshape(2,3))

# convert any dimension array to one dimension
print("flate to one dimension:",a.ravel())
print("ravel does not convert the original array you have to store it to other variable to use it:",a)

# mathematical methods
print("min:", a.min())
print("max:", a.max())
print("sum:", a.sum())
print("axis sum:", a.sum(axis=0)) # column is 0 axis and row is at 1 axis
print("axis sum:", a.sum(axis=1))
print("square root:", np.sqrt(a))
print("standard deviation:", np.std(a))

a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
print(a+b)
print(a*b)
print(a/b)
print("matrix product:", a.dot(b))