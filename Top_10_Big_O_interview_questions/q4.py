# what is the runtime of the below code?
def printUnorderpairs(arrayA,arrayB):
    for i in range(len(arrayA)):  # Big_O = O(len of arrayA)
        for j in range(len(arrayB)):  # Big_O = O(len of arrayB)
            if arrayA[i] < arrayB[j]:  # Big_O = O(1)
                print(arrayA[i],'and',arrayB[j]) # Big_O = O(1)
# total = Big_O = O(len of arrayA * len of arrayB)