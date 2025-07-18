a = [1,2,3,4] 
b = [5,6,7,8]


# another two array and merge them into one 
def mergetarrays(a, b):
    c = []
    for i in range(0 , len(a)):
        c.append(a[i])
 
    for j in range(0 , len(b)):
        c.append(b[j])

    return c

print(mergetarrays(a, b))

# Merge arrays 
# TIme complexity  = O(n)
# Space complexity = O(n)