# what is the runtime of the below code?
def printUnordPairs(array):
    for i in range(0,len(array)):  # Big_O = O(n)
        for j in range(i+1,len(array)): # Big_O = O(n/2)
            print(array[i] ,'and',array[j])  # Big_O = O(1)
# total = O(n)*O(n/2)+O(1) = O(n**2)