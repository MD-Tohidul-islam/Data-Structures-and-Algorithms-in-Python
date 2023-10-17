mydict= {'name':'Edy','age':27,'adress':'london'}
# mydict.clear()
# print(mydict)

dict1 = mydict.copy()
print(dict1)
#  fromkeys() methods
# dict2 = {}.fromkeys([1,2,3,4],0)
# print(dict2)

# get() method
# print(mydict.get('country'))
# # item() method
# print(mydict.items())
# keys() method : return all keys of dictionary
# popitem()
# print(mydict.popitem())
# print(mydict)
# setdefault()
# print(mydict.setdefault('name','added'))
# print(mydict.setdefault('name1','added'))
# pop()
# print(mydict.pop('name','not'))
# print(mydict)
# values() method
print(mydict.values())
# update() it takes other dictionary or tuple
newDict = {'a':1,'b':2,'c':3}
mydict.update(newDict)
print(mydict)
