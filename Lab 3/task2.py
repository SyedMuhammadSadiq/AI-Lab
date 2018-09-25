# import math
# x = int(input("Enter num1:"))
# y = int(input("Enter num2:"))
# op = input("Enter operator:")
# if(op=='+'):
#     ans = x+y
#     print("Answer:",+ans)
# elif(op == '-'):
#         ans = x - y
#         print("Answer:", + ans)
# elif(op=='*'):
#     ans = x*y
#     print("Answer:",+ans)
# elif (op == '/'):
#         ans = x / y
#         print("Answer:", + ans)
# else:
#     if print("Invalid"):


def addition(x,y):
    print("add =  ",x + y)

def substract(x,y):
    print("subs =  ",x - y)

def multiplu(x, y):
        print("mul =  ", x * y)


def divide(x, y):
    print("div =  ", x / y)

x = int(input("Enter num1:"))
y = int(input("Enter num2:"))

addition(x,y)
substract(x,y)
multiplu(x,y)
divide(x,y)