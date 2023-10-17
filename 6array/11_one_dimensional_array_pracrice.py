from array import *
#  creating a array and traverse
my_array = array('i',[1,2,3,4,5])
for i in my_array:
    print(i)
#  access individual elements through indexes
print('accessing')
print(my_array[0])
print(my_array[4])
print('appending')
my_array.append(6)
print(my_array)
print('inserting')
my_array.insert(0,11)
my_array.insert(3,12)
print(my_array)
print('extending')
my_array1 = array('i',[10,14,15])
my_array.extend(my_array1)
print(my_array)
print('add items from list')
templist = [20,21,22]
my_array.fromlist(templist)
print(my_array)
print('removing first occur items')
my_array.remove(11)
print(my_array)
print('poping')
my_array.pop()
print(my_array)
print('fetch any element through its index')
print(my_array.index(21))
print('reversing')
my_array.reverse()
print(my_array)
print('get array buffer information through buffer_info()')
print(my_array.buffer_info())
print('counting')
print(my_array.count(12))
print('converting array to string using tostring()')
strTemp = my_array.tostring()
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(ints)
print('converting array into a python list using tolist()')
print(my_array.tolist())
print('appending a string to char array using fromstring()')
print('slice element from an array')
print(my_array[1:4])


