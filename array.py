from array import *
vals=array('i',[3,6,9,11])

for i in range(0,len(vals)):
    print(vals[i])

for e in vals:
    print(e)

values =array('u',['a','e','i'])
for e in values:
    print(e)

#copy values from one array to another
newArr= array(vals.typecode,(a*a for a in vals))
i=0
while(i<len(newArr)):
    print(newArr[i])
    i+=1
#create array from user input
arr=array('i',[])
x=int(input("Please enter the length of the array"))
for i in range(x):
    y=int(input("Enter the next value"))
    arr.append(y)

print(arr)
#user will enter a number and we will try to find out index of that
a=int(input("Please enter the number you want to find index in arra"))
print(arr.index(a))
# for i in range(len(arr)):
#     if(a.__eq__(arr[i])):
#         print("the index value is",i)
#         break
# else:
#     print("number not present in array")