def fibonacci(n):
    if n >=0 and int(n) == n:
        if n == 0 or n==1:
            return n
        else:
            return fibonacci(n-1)+fibonacci(n-2)
    else:
        print('number must be integer')

print(fibonacci(7))