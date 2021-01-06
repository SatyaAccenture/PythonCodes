from numpy import *
arr1=array([6,7,8,9,10,13])
arr2=array([15,13,9,3,21,7])
i=len(arr2)
arr3=zeros(i,int)
for a in range(0,i):
 arr3[a]=arr1[a]+arr2[a]
 a+=1
print(arr3)
#sorting
# for a in range(0,i):
#     for b in range(a+1,i):
#       temp=0
#       if arr3[a] > arr3[b]:
#         temp=arr3[b]
#         arr3[b]=arr3[a]
#         arr3[a]=temp
#         b+=1
#     a += 1

print(arr3)
#max element
max=0
for a in range(0,i):
    if arr3[a] > max :
        max=arr3[a]
    a += 1


print(max)