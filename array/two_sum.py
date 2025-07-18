# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# The array is unsorted
# We can safely assume that there is a single result here
# no repeats are present


# Mistakes:
# Not being able to understand how to set up my for loops to iterate over the array
# Made a mistake a in the variable names 
# Forgot to print

# def twosum(arr, result):
#     for i in range(0, len(arr)):
#         for j in range(i + 1, len(arr)):
#             if(arr[i] + arr[j] == result):
#                 return [i, j]
#     return False

# print(twosum(nums, target))

# Time complexity of O(N^2)
# Space complexity is O(1)

# Second approach
# Can you keep track of the numbers you've already 
# seen as you loop once through the array?


# Second approach
# Use a set
# Check if that number is in the set 
# if not then take the target number - that with the current looping number and add
# it to the set

nums = [2,5,11,15]
target = 9

def two_sum(arr, result):
    seen = set()
    for i in arr:
        if i in seen:
            return True
        seen.add(target - i)
    return False

print(two_sum(nums, target))