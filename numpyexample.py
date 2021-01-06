from numpy import *
import numpy as np

# arr = array([1,3,5,7,9],float)
#arr=linspace(1,16,20)
#by default linespace have 50 parts that is the 3rd arg
#arr=arange(1,15,2)
#arr=logspace(1,40,5)
#print('%.2f' %arr[0])
# print(arr)
# print(arr.dtype)
# arrzero=zeros(5)
# arrones=ones(5,int)
# print(arrones)
# print(concatenate([arr,arrones]))
arr1=array([2,6,8,7,6])
arr2=arr1.copy()
# view function is used for shallow copy.For deep copy we use .copy()
# arr1[1]=7
# print(id(arr1))
# print(id(arr2))
# print(arr1)
# print(arr2)

arr1=array([6,7,8,9,10,13])
arr2=array([15,13,9,3,21,7])
i=len(arr2)
arr3=zeros(i,int)
for a in range(0,i):
 arr3[a]=arr1[a]+arr2[a]
 a+=1
print(arr3)



print(arr3)
#max element
max=0
for a in range(0,i):
    if arr3[a] > max :
        max=arr3[a]
    a += 1


print(max)