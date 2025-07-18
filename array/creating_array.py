strings = ['a','b','c','d']

# Push = append 
strings.append('e') #O(1)

# Pop
strings.pop()
strings.pop()

# unshift
strings.insert(0, 'x')

strings = strings[0:3]

print(strings)