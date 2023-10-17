# what is the runtime of the below code?
def printunorderpairs(arrayA, arrayB):
    for i in range(len(arrayA)):# O(len of arrayA)
        for j in range(len(arrayB)):# O(len of arrayB)
            for k in range(0,10000): # O(1)
                print(str(arrayA[i]), str(arrayB[j])) # O(1)
# total Big_O = O(len of arrayA*len of arrayB)+o(1)+O(1)=O((len of arrayA*len of arrayB)