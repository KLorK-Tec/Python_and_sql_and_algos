#--------------------------------------------
def selection_sort(arr):
    for i in range(len(arr)):
        minin = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minin]:
                minin = j
        arr[i],arr[minin] = arr[minin],arr[i]
    return arr
#--------------------------------------------
def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            break
    return arr
#--------------------------------------------
def insertion_sort(arr):
    for i in range(len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr
#--------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #finds middle
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res
#--------------------------------------------
def binary_search(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    


print(selection_sort([1,5,3,4,6]))
print(bubble_sort([1,5,3,4,6]))
print(insertion_sort([1,5,3,4,6]))
print(merge_sort([1,5,3,4,6]))
print(binary_search([1,2,3,4,5],4))