#  how to find muximum product of two integer in the list or array
#  where all element are positive
import numpy as np
myarray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def max_product(array):
    maxproduct= 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j] > 0:
                maxproduct = array[i]*array[j]
                pairs = (array[i],array[j])
    return maxproduct,pairs
print(max_product(myarray))