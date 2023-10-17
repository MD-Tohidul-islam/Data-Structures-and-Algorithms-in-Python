def power(x,n):
    if n>=0 and int(n) == n:
        if n==0:
            return 1
        if n==1:
            return x
        return x*power(x,n-1)
    return ('power must be positive integer ')

print(power(2,-2))