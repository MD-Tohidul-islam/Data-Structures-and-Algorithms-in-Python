#  Is unique implement an algorithm to determine if a list has all
#  unique characters, using python list.

mylist = [1,2,3,4,5,6,7,8,9,10,12,13,3,14,15,16,17,18,19,20]

def Is_unique_lsit(alist):
    a = []
    for i in alist:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(Is_unique_lsit(mylist))