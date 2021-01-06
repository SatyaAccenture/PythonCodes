#
#
# x=int(input("Enter first number"))
# y=int(input("Enter second number"))
# z=x+y;
# print(z);
#
# result=eval(input("enter an expression"))
# print(result)
#
# x=int(input("enter a number"))
# r = x % 2
#
# if(r==0):
#     print("even")
#     if(x > 5):
#         print("greater")
#     else :
#         print("less")
# else:
#     print("odd")
#
# i=1
#
# while i<=5:
#     print("hello", end="")
#     j=1
#     while j<=4:
#         print("world", end="")
#         j=j+1
#     i+=1
#     print()
#
#
# for i in range(10):
#     print(i)

#candy vending machine
# av=5
# i=1
# x=int(input("how many candies you want?"))
#
# while i<=x :
#     if i>av:
#         print("out of stock")
#         break
#     print("candy")
#     i+=1
#
# print("thank you!Visit again!")


# for i in range(1,101):
#     if(i%3==0) and (i%5==0):
#         continue
#
#     print(i)
#
# print("End of Loop")

#pass example
# for i in range(1,21):
#
#     if(i%2==0):
#         pass
#     else:
#         print(i)


#pattern printing

# i=1
# while i<=4:
#     j=1
#     while j<=4-i+1:
#         print("#",end="")
#         j+=1
#     i+=1
#     print()


# for else
nums = [12,16,18,22,26]
for i in nums:
    if(i%5==0):
        print(i)
        break
else:
    print("not found")
