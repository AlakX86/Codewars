def first_n_smallest(arr, n):
    sortedList = sorted(arr)
    workList = sortedList[:n]
    #workList será una lista temporal, para trabajar sobre ella, no se muy bien como nombrarlo. Aun que creo que no se debería hacer.
    index = []
    for i in range(len(arr)):
        if arr[i] in workList:
            index.append(i)
            workList.remove(arr[i])
    counter = 0
    finalList = []
    while counter < n:
        finalList.append(arr[index[counter]])
        counter += 1
    return finalList