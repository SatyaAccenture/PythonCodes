import math;
num = int(input("Enter a number"))
max_div = math.floor(math.sqrt(num))
if num<=1:
    print("Not Prime")
else:
    for i in range(2,max_div+1):
      if num%i ==0:
        print("Not Prime")
        break
    else:
      print("Prime")