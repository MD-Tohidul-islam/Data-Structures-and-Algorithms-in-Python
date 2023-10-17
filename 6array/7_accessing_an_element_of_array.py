from array import *
arr1 = array('i',[1,2,3,4,5])
print(arr1[3])
def accessing_element(array,index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])
accessing_element(arr1,5)