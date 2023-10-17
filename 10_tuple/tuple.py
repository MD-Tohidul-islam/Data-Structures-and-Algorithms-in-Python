# create a tuple
# tuple is immutable
newtuple = ('a','b','c','d','e')

newtuple1 = ('a',)
print(newtuple)
print(newtuple1)

newtuple2 = tuple('abcdef')
print(newtuple2)

# accessing an element of tuple : i know that

# traversing a tuple: i know that

#  search for an element in tuple : i know that
def searchTuple(ptuple,element):
    for i in ptuple:
        if i == element:
            return ptuple.index(i)
    return 'the element does not in the tuple'
print(searchTuple(newtuple2,'c'))
