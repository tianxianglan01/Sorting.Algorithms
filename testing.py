def isEqual(func):
    count = 0 
    lstA = [1, 3, 1, 2, 7, 4]
    lstB = [3, 12, 4, 98, 2, 3]
    aSorted = sorted(lstA)
    bSorted = sorted(lstB)
    if func(lstA) == aSorted:
        count += 1
    if func(lstB) == bSorted:
        count += 1
    
    if count == 2:
        return 'Sorted!'
    else:
        return 'Not Sorted!'

print(isEqual())

