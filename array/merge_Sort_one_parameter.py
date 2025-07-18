class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_side_arr = self.mergeSort(nums[:mid])
        right_side_arr = self.mergeSort(nums[mid:])
        return self.merge(left_side_arr, right_side_arr)

    def merge(self, a, b): 
        sorted_list = []
        left = right = 0

        while left < len(a) and right < len(b):
            if a[left] < b[right]:
                sorted_list.append(a[left])
                left += 1
            else:
                sorted_list.append(b[right])
                right += 1

        while left < len(a):
            sorted_list.append(a[left])
            left += 1

        while right < len(b):
            sorted_list.append(b[right])
            right += 1

        return sorted_list

sol = Solution()
arr = [7, 4, 1, 5, 3]
print(sol.mergeSort(arr))  # ✅ Output: [1, 3, 4, 5, 7]
