import numpy as np

n = [6,7,8]
print(n[0:2])
print(n[-1])

a = np.array([6,7,8])
print("a value:", a[0:2])
print(a[-1])

a = np.array([[6,7,8], [1,2,3], [9,3,2]])
#print the from 2nd row the 3rd element
print(a[1,2])
# now go from 0 to 2nd row and print the 2nd element of both
print(a[0:2, 2])

print("last row:",a[-1])
#prints from the last row the first 2 elements
print(a[-1,0:2])
#now go from all the row and print values from 2nd to 3rd element of each row
print(a[:,1:3])

#iterate
for row in a:
    print("row:",row)
# flat the array and print elements like single dimension array
for cell in a.flat:
    print("elements:", cell)

#stacking the array
a = np.arange(6).reshape(3,2)
b = np.arange(6, 12).reshape(3,2)
print("first:", a)
print("2nd:", b)
#stacking one array to another = vertical stacking
print("Stacking:", np.vstack((a,b)))
# horizontal stacking
print("vertical stacking:",np.hstack((a,b)))

a = np.arange(30).reshape(2,15)
#split the array in 3 equal size array
result = np.hsplit(a,3) #horizontal split

print("split:", result)
print("single:",result[0])

result = np.vsplit(a,2) #vertical split

print("vertical split:", result)
print("single:",result[0])

#indexing with boolean arrays
a = np.arange(12).reshape(3,4)
print("aaray:", a)

b = a > 4
print("values true greater than 4 in array:", b)

# extracts all the elements which are greater than 4
print("print the only true element: ",a[b])

# any element which are greater then 4 replace it with other value
a[b] = -1

print("array will be:", a)