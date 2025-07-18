a = [1,2,3,4] 
b = [5,6,7,8]

# def mergetarrays(a, b):
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])

#     for j in range(len(b)):
#         c.append(b[j])

#     # Proper selection sort
#     for z in range(len(c) - 1):
#         min_index = z
#         for x in range(z + 1, len(c)):
#             if c[x] < c[min_index]:
#                 min_index = x
#         c[z], c[min_index] = c[min_index], c[z]

#     return c

#Time complexity : O (N^2)
# Space complexity : O (N)

# another two array and merge them into one 
# def mergetarrays(a, b):
#     c = []
#     for i in range(0 , len(a)):
#         c.append(a[i])
 
#     for j in range(0 , len(b)):
#         c.append(b[j])

#     c.sort()
#     return c

# print(mergetarrays(a, b))
# # Time complexity: O(N) * log(N)
# # Space compelxity O(n)

def mergetarrays(a, b):
    return sorted(a + b)


print(mergetarrays(a,b))
