#recursion algorithm
def algorithm_sum(a,n):
    if n == 1:
        return a[0]
    s = algorithm_sum(a,n-1) # recurse on all but last
    s = s+a[n-1]
    return s
a = [10,2,3,4,5,6,7,8,9]
print(algorithm_sum(a,n=3))