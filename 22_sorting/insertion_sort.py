def insertionSort(customlist):
    for i in range(1, len(customlist)):
        key = customlist[i]
        j = i-1
        while j>=0 and key < customlist[j]:
            customlist[j+1] = customlist[j]
        customlist[j+1] = key
    print(customlist)

clist = [2,1,7,6,5,3,4,9,8]
print(insertionSort(clist))