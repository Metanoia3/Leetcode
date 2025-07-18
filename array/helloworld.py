import time 
array = [1, 2, 3, 4, 5]
array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

large_array = [5] * 100000  

def find_5(array):
    t0 = time.time() 
    for i in range(0, len(array)):
        if(array[i] == 5):
            print("found 5")
    t1 = time.time()
    print ("time taken: ", t1 - t0)

find_5(large_array)