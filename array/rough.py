def selection_sort(array):
    for i in range(0, len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if(array[min] > array[j]):
                min = j
        array[i], array[min] = array[min], array[i]
    return array

a = [9,7,5,4,2]

print(selection_sort(a))