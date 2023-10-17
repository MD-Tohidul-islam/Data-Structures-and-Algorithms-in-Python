import numpy as np
day1 =[11,15,10,6]
day2 = [10,14,11,5]
day3 = [12,17,112,8]
day4 = [15,18,14,9] 
two_dimensional_array = np.array([day1,day2,day3,day4])
print(two_dimensional_array)

def travers_two_D_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j])
print(travers_two_D_array(two_dimensional_array))