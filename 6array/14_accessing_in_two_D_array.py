import numpy as np
day1 =[11,15,10,6]
day2 = [10,14,11,5]
day3 = [12,17,112,8]
day4 = [15,18,14,9]
two_dimensional_array = np.array([day1,day2,day3,day4])
print(two_dimensional_array)
def accesses_element(array,row_index,column_index):
    if row_index >=len(array) and column_index>= len(array[0]):
        print('Incorrect index')
    else:
        print(array[row_index][column_index])
print(accesses_element(two_dimensional_array,1,2))