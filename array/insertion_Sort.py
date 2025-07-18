# WHAT I UNDERSTOOD ABOUT INSERTION SORT:
# INSERTION SORT IS BASICALLY WHEN THERE IS AN ARRAY SAY FOR EXAMPLE [5,2,3,4,1] AND THEN THE ARRAY CHECKS IF
# 2 IS IN ITS CORRECT POSITION NAD THEN SWAPS THEN CHECK IF 3 IS IN ITS CORRECT POSITION FINALLY THESE SINGLE SWAPS 
# KEEP HAPPENING UNTIL IT REACHES 1 AND THEN 1 IS CHECKED THROUGHOUT AND EVERYONE RIGHTSHIFTS TO MAKE PLACE FOE ONE 


# What I learnt from insertion:
# How you can iteratively make an array keep checking the previous 
# How to basically go back and forth the array which is beautiful 

def insertionSort(arr):
    for i in range(0, len(arr)):
        j = i
        while(j > 0  and arr[j-1] > arr[j]):
            arr[j-1] , arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

array = [5,4,3,211,1]
print(insertionSort(array))


        
