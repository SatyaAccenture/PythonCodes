import sys
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2=add_sub(8,5)
print(result1,result2)

def update(x):
    print(id(x))
    x=8
    print("x",x)


a=10
print(id(a))
update(a)
print("a",a)

def person(name,age=18):
    print(name)
    print(age)

person(name='Navin')

#calculation with variable number of input args
def add(*b ):
    c=0
    for i in b:
        c+=i

    return c

print(add(6,8,9,10))
#keyworded variable length argument
# def person(**data):
#     for i,j in data.items() :
#         print(i,j)
#
#
# person(name='Satya',age=26,city='Mumbai',mob=7407841204)

#local and global variable
# a=10
#
# def something():
#     a=9
#     globals()['a']=15
#     print("inside",a)
#
#
# something()
# print("outside",a)
#user input list
# arr= []
# size=int(input("Please enter how many names you want"))
#
# for i in range (0,size):
#     x=input("please enter next name")
#     arr.append(x)
#
# def length(arr):
#     greater = 0
#     for a in arr:
#         if len(a) >5:
#             greater+=1
#
#     return greater
#
# great = length(arr)
# print("greater : {}".format(great))


def fib(n):
    a = 0
    b = 1
    if n < 10:
        return "the input number should be positive"
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        c=0
        while a+b < n:
            c=a+b
            a=b
            b=c
            print(c)


fib(100)
print()
print(fib(-2))

sys.setrecursionlimit(2000)
i = 0
def fact(n):
    if n < 0:
        return ("please enter a validnumber")
    else:
        if n==0:
            return 1
        else:
            return n* fact(n-1)

print(fact(5))

print("Hello"+ __name__)