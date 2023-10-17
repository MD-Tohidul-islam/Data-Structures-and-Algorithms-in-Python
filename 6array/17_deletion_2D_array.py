import numpy as np
day1 =[11,15,10,6]
day2 = [10,14,11,5]
day3 = [12,17,112,8]
day4 = [15,18,14,9]
two_dimensional_array = np.array([day1,day2,day3,day4])
print(two_dimensional_array)
new_2D_array = np.delete(two_dimensional_array,0,axis=0) # axis=0 means row and axis = 1 means column
print(new_2D_array)