import math

def insertionSort(customlist):
    for i in range(1, len(customlist)):
        key = customlist[i]
        j = i-1
        while j>=0 and key < customlist[j]:
            customlist[j+1] = customlist[j]
        customlist[j+1] = key
    print(customlist)

def bucketSort(customlist):
    number_of_buckets = round(math.sqrt(len(customlist)))
    maxValue = max(customlist)
    arr = []

    for i in range(number_of_buckets):
        arr.append([])

    for j in customlist:
        index_b = math.ceil(j*number_of_buckets/maxValue)
        arr[index_b-1].append(j)

    for i in range(number_of_buckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            customlist[k] = arr[i][j]
            k+=1
    return customlist

