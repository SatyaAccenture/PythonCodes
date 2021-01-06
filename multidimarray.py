from numpy import *
arr1=array([
    [1,2,3],
    [7,8,9]
])
# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
# arr2=arr1.flatten()
# print(arr2)
#arr3=arr2.reshape(3,4)
# arr3=arr2.reshape(2,2,3)
# print(arr3)
m= asmatrix(arr1)
# print(m)
# print(diagonal(m))
# print(m.min())
# print(m.max())
m1=asmatrix('1,2,3;4,5,6;7,8,9')
m2=asmatrix('2,4,6,8;4,6,8,10;6,8,10,12')
m3=m1  * m2
print(m3)
#algo to matrix multiplication
rows = len(m3)
columns = len(m3.transpose())
print(rows)
print(columns)