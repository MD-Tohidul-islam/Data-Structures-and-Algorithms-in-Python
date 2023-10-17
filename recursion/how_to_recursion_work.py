# def firstMethod():
#     secondMethod()
#     print('i am the first methodj')
# def secondMethod():
#     thirdMethod()
#     print('i am the second method')
# def thirdMethod():
#     firstMethod()
#     print('i am the third method')
# def fouthMethod():
#     print('i am the fouth method')
def recursiveMethod(n):
    if n<1:
        print('n is less than 1')
    else:
        recursiveMethod(n-1)
        print(n)
print(recursiveMethod(10))

