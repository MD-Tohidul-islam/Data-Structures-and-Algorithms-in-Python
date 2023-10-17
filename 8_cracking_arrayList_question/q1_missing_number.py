#  question: how to find the missing number in an integer array of 1 to 100
mylist = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
def find_missing(alist,n):
    sum1 = (n*(n+1))/2
    sum2 = sum(alist)
    missing_number = sum1-sum2
    return missing_number
print(find_missing(mylist,20))
