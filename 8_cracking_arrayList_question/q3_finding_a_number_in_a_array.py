#  how to check if an array contains a number in python
import numpy as np
myarray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def find_number(array,number):
    for i in range(len(array)):
        if array[i] == number:
            return i
print(find_number(myarray,13))
