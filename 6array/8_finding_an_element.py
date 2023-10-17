from array import *
arr1 = array('i',[1,2,3,4,5])
def finding_an_element(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    else:
        return 'The element does not exist in this array'
print(finding_an_element(arr1,0))