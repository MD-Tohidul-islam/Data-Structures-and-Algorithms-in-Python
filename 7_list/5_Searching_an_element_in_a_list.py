# in operator : i know that

# liner operation:
l = [1,2,3,4,5]
def liner_search(alist,value):
    for i in alist:
        if i == value:
            return alist.index(value)
    return 'the value does not exist in the list'

print(liner_search(l,3))
