# Implement selection sort, insertion sort and bubble sort


# Bubble sort works on adjacent swapping basically if we have an array it 
# It check the if the a[i] is less than a[i+1] then swap
def bubblesort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) -i - 1):
            if(arr[j+1]<arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr

array = [5,4,3,6,7,2,1]
print(bubblesort(array))

# Insertion sort basically works where you take a number and insert it into 
# the correct position 

# Selction sort is basically where you take the max and swap it till the end

def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arrae = [4, 7, 5, 2, 4, 1, 6]
print(selectionsort(arrae))
