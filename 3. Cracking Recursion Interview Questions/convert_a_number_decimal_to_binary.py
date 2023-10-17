def decimal_to_binamry(n):
    assert int(n)==n,'the parameter must be integer'
    if n==0:
        return 0
    return n%2+10*decimal_to_binamry(int(n/2))
print(decimal_to_binamry(10))