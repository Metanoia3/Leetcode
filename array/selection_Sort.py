def selection_Sort(arr):
    for i in range(0, len(arr)- 1):
        min = i
        for j in range(i + 1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

array = [5,4,3,2,1]
print(selection_Sort(array))

#### Do this again you need to perfect such questions they help youi think
