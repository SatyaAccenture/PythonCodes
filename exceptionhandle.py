a=5
b=2

try:
    c=a/b
    print(c)
    d=int(input("Enter a Number"))
    print(d)
except ZeroDivisionError as e:
    print("Can not devide by zero",e)
except ValueError as e:
    print("Invalid input",e)
except Exception as e:
    print("Something went wrong",e)
finally:
    print("resource closed")
print("bye")