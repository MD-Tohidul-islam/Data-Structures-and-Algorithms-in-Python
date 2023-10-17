def factorial(n):
    #assert n>=0 and int(n) == n, 'the number must be positive integer only'
    if n == 1 or n==0:
        return 1
    else:
        return factorial(n-1)*n
print(factorial(5))