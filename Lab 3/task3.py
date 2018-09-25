# import math
# for i in list(range (1,21)):
#     list=i*i
#     print(list)
#
#
list = []

def abc(x,y):
    for i in range(x, y):
        list.append(i * i)
    print(list)

abc(1,21)