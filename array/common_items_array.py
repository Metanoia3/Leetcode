# /*Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# should return false.
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# should return true. */


# Parameters two arrays - no size limit 
# Returns true or false 



# def common_items(array1, array2):
#     for i in range(0, len(array1)):
#         for j in range(0, len(array2)):
#             if(array1[i] == array2[j]):
#                 return True 
    
#     return False 

# print(common_items(array1, array2))

# Time complexity: O(A*B)
# Space complexity : O(1)

array1 = ['a', 'b', 'c', 'x'] 
array2 = ['z', 'y', 'x']

def contains_common_items(arr1, arr2):
    #loop through the first array and create and object where properties == items in the array
    # Loop throught the second array and  check if item in the second array exits on created object

    # Mistake I made was that this:
    # Loop1 : for i in range(0, len(arr1)):
                # map[i] = True
    # Result: map = {0: True, 1: True, 2: True}

    # Correction loop:
    #           for item in arr1:
    #             map[item] = True
    # Result: map = {'a': True, 'b': True, 'c': True}

    map = {} 
    for item in arr1:
        map[item] = True
    
    print(map)

    for j in range(0, len(arr2)):
        if arr2[j] in map:
            return True    
    return False

print(contains_common_items(array1, array2))

# Time complexity: O(A*B)
# Space complexity : O(1)