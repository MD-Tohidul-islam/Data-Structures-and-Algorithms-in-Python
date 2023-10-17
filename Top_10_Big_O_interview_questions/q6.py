# what is the runtime of the below code?
def reverse(array):
    for i in range(0,int(len(array)/2)):  # O(n/2)=O(n)
        othe = len(array)-i-1  # O(1)
        temp = array[i]  # O(1)
        array[i] = array[othe]  # O(1)
        array[othe] = temp  # O(1)
    print(array)  # O(1)
array = [3,4,5,6,78,6,5,3,2]
print(reverse(array))
# total Big_O = O(n)
