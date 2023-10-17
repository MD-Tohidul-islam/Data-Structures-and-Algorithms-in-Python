def gcd(a,b):
    assert int(a)==a and int(b) == b, 'the must be integer'
    if a<0:
        a= -1*a
    if b<0:
        b = -1*b
    if b==0:
        return a


    return gcd(b,a%b)