def repeats(arr):
    addArray=0
    for num in arr:
        if arr.count(num)>1:
            pass
        else:
            addArray += num
    return addArray