# # Observation while seeing bubble sort work:
# # What I saw was basically in this algorithm there are two pointers one points @1st element say this i 
# and the other is i + 1, you keep swapping them if say arr[i] > arr[i+1] you swap there (adjacent swapping)
# so in the firt iteration generally if you intuitively think about it the maximum element will come to the last
# position in the second iteration the second last and so on. So this is how basically the array sorts itself 

# this will be the code according to me 

# My attempt which is wrong 
# def bubble_Sort(array):
#     first_element = 0
#     for z in range(0, len(array)):    
#         for i in range(1, len(array)):
#             if(array[first_element] > array[i]):
#                 array[first_element], array[i] = array[i], array[first_element]
#             first_element += 1
#     return array

# a = [7,6,5,4,3,2,1]    
# print(bubble_Sort)


# Correct implementation

def bubble_Sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]

    return array

a = [8,7,6,5,4,32,1]

print(bubble_Sort(a))