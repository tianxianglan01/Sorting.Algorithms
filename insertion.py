from testing import isEqual

def insertionSort(lst):
    for i in range(1, len(lst)):
        # start from 1
        key = lst[i]
        j = i - 1
        # as long as j's value is >= 0 and lst[i] <= lst[j] where j is the previous element
        # 
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key