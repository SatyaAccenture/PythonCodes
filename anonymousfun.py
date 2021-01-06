from functools import reduce

import function
from function import *
f = lambda a,b : a+b
print(f(5,6))
nums=[2,4,7,9,11,8,6]
evens=reduce(lambda a,b: a+b,map(lambda a: a*a,filter(lambda a: a%2==0,nums)))

print(evens)
#decorators in python
def div(a,b):
    print(a/b)

def smart_div(function):
    def inner_div(a,b):
        if a<b:
            a,b=b,a
        return function(a,b)

    return inner_div

div=smart_div(div)
div(6,12)
print(function.fib(10))
print("Hello"+ __name__)