#  what is the runtime of the below code?
def printPairs(array):
    for i in array:  # Big_O = O(n**2)
        for j in array:  # Big_O = O(n)
            print(f'{i} and {j}')  # Big_O = O(1)
# total Big_O = # O(n)*O(n) + O(1) = O(n**2)
