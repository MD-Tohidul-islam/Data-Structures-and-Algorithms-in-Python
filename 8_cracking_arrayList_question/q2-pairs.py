#  write a program to find all pairs of integer whose sum is equal to a
# given number
mylist = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
def find_pairs(alist,sum):
    for i in range(len(alist)):
        for j in range(i+1,len(alist)):
            if alist[i]+alist[j] == sum:
                return (alist[i],alist[j])
print(find_pairs(mylist,6))