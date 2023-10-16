def comp(array1, array2):
    if array1 == None:
        return False
    elif array2 == None:
        return False
    elif len(array1) != len(array2):
        return False
    array3 = []
    for i in range(len(array1)):
        array3.append(array1[i] ** 2)
    array2.sort()
    array3.sort()
    if array3 == array2:
        return True
    else:
        return False