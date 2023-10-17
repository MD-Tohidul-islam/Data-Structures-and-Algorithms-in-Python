def findMaxNumber(sample_list,n): #  Big_O = M(n)
    if n == 1: # Big_O = O(1)
        return sample_list[0]  #  Big_O = O(1)
    return max(sample_list[n-1],findMaxNumber(sample_list,n-1)) # Big_O = M(n-1)
#M(n) =O(1) + M(n-1)
#M(1) = O(1)
# M(n-1) = O(1) + M((n-1)-1))
# total = Bio_O = O(n)