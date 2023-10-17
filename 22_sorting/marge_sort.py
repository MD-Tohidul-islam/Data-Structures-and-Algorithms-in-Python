def merge(customlist,first_index,middle_index,last_index):
    n1 = middle_index - first_index+1
    n2 = last_index - middle_index

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0,n1):
        L[i] = customlist[first_index+i]
    for j in range(0,n2):
        R[j] = customlist[middle_index+1+j]

    i = 0
    j = 0
    k = first_index
    while i< n1 and j< n2:
        if L[i]<=R[j]:
            customlist[k] = L[i]
            i+=1
        else:
            customlist[k] = R[j]
            j+=1
        k+=1
    while i< n1:
        customlist[k] = L[i]
        i+=1
        k+=1
    while j<n2:
        customlist[k] = R[j]
        j+=1
        k+=1

def mergeSort(customList, l,r):
    if l<r:
        m = (l+(r-1))//2
        mergeSort(customList,l,m)
        mergeSort(customList,m+1,r)
        merge(customList,l,m,r)
    return customList

clist = [2,1,7,6,5,3,4,9,8]
print(mergeSort(clist,0,8))



