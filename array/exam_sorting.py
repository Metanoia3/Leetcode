class Solution:
    def selectionSort(self,arr):
        for i in range(0, len(arr)):
            min = i
            for j in range(i + 1, len(arr)):
                if(arr[j] < arr[min]):
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr
    
    def bubbleSort(self, arr):
        for i in range(0, len(arr)):
            for j in range(0, len(arr) - i - 1):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr
    
    def InsertionSort(self,arr):
        
    
sol = Solution()
arr = [6,4,2,8,4,2,1,7,9,6,3,1]
print(sol.selectionSort(arr))
print(sol.bubbleSort(arr))
