def sumofDigits(n):
    if n>=0:
        if n<10:
            return n
        else:
            return int(n%10) + sumofDigits(int(n/10))
    else:
        return ('number must be positive')
print(sumofDigits(10))
def sumofDigits1(n):
    assert n>=0 and int(n) == n , 'the number must to be positive'
    if n==0:
        return n
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits1(10))