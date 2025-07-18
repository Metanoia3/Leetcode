array = [3,2,3]

def majorityelement(arr):
    storer = 0 
    for i in range(0, 10):
        counter = arr.count(i)
        if(storer < counter):
            storer = counter
    return storer

print(majorityelement(array))