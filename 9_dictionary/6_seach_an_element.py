mydict= {'name':'Edy','age':27}

def seachDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'the value does not exist'

print(seachDict(mydict,27))
