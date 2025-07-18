def k_rotate(nums,  k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

def k_rotate(nums, k):
    
arr = [1,2,3,4,5,6,7]
b = 3
print(k_rotate(arr, b))

