def findBiggestNumber(sample_array):
    biggest_number = sample_array[0] # Bog_O = O(1)
    for index in range(1,len(sample_array)): # Big_O = O(n)
        if sample_array[index]>biggest_number: # Big_O = O(1)
            biggest_number = sample_array[index]  # Big_O = O(1)
    print(biggest_number)  # Big_O = O(1)

#  Big_O = sum of Big_O = O(1)+O(n)+O(1)+O(1)+O(1)+O(1) = O(n)

