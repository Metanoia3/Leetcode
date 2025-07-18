# # Creat a funtion that basically reverses a string

# Input: "hello"
# Output: "olleh"

# Input: "12345"
# Output: "54321"

# A fucntion that reverses the string
#

# Mistakes I made while coding this:



# def reverse_a_string(string):
#    for i in range(len(string) - 1 , -1 , -1):
#        print(string[i])

# # O(n) Time 
# # O(1) Space

def reverse_a_string(string):
    return string[len(string)-1::-1]


# O(N)
# O(n)
print(reverse_a_string("hello"))