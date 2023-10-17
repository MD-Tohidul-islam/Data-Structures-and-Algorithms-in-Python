import numpy as np
day1 =[11,15,10,6]
day2 = [10,14,11,5]
day3 = [12,17,112,8]
day4 = [15,18,14,9]
two_dimensional_array = np.array([day1,day2,day3,day4])
print(two_dimensional_array)
new_two_D_array= np.insert(two_dimensional_array,0,[[1,2,3,4]],axis=1)
# here if axis = 1 than it add to column
print(new_two_D_array)
new_two_D_array1= np.insert(two_dimensional_array,0,[[5,6,7,8]],axis=0)
# and if axis = 0 than if add to row
print(new_two_D_array1)
print()
new_two_D_array2 = np.append(two_dimensional_array,[[1,2,3,4]],axis=0)
print(new_two_D_array2)