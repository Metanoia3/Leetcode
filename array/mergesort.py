def mergeSort(arr, low, high):
    if(low >= high):
        return arr
    mid = (low + high)// 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while(left <= mid and right <= high):
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while(left <= mid):
        temp.append(arr[left])
        left += 1

    while(right <= high):
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


arr1 = [6, 2, 8, 5, 3]
mergeSort(arr1, 0, len(arr1) - 1)
print(arr1)  # Expected: [2, 3, 5, 6, 8]



