
def permutation(list1,list2):
    list2.reverse()
    if list1 == list2:
        return True
    else:
        return False
l1 = [1,2,3]
l2 = [3,2,1]
print(permutation(l1,l2))