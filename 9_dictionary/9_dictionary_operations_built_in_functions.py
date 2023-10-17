mydict= {'name':'Edy','age':27,'adress':'london'}
#  in opetator()
print('name' in mydict)
print('Edy' in mydict)
print('Edy' in mydict.values())

# for operation
for key in mydict:
    print(key,mydict[key])
print()
# all() method : all(dictionary)
new_dict = {0:False,1:True,2:True}
print(all(new_dict))

# any() : any(dictionary)
print(any(new_dict))
print()

# len() method: len(dictionary) : i know that
# sorted() method: i know that
# reverse() method: i know that
print(sorted(mydict,key = len))