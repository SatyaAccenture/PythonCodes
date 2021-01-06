
num=[6,8,5,3,1,99,67,45,4]
num2=sorted(num)
index=-1
def binary(list,n):
    l=0
    u=len(num2)-1


    while l <= u:
            m = (l + u) // 2
            if num2[m]==n:
                globals()['index'] =m
                return True
            else:
                if num2[m] < n:
                    l=m+1
                else:
                    u=m-1

    return False




if binary(num2,100):
    print("Item Found at",index)
else:
    print("Item not found")