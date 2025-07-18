class Solution:
    def SelectionSort(self, arr):
        for i in range(0, len(arr) - 1):
            min = i 
            for j in range(i + 1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[min], arr[i] = arr[i], arr[min]
        return arr
    
    def bubbleSort(self, arr):

        for i in range(0, len(arr) - 1): 
            for j in range(0, len(arr) - i - 1):
                if(arr[j] > arr[j+1]):
                    arr[j] , arr[j+1] = arr[j+1], arr[j]
        return arr
    
    def insertionSort(self, arr):
        for i in range(0, len(arr)):
            j = i
            while(j > 0 and arr[j-1] > arr[j]):
                arr[j-1] , arr[j] = arr[j], arr[j+1]
                j -= 1
        return arr

sol = Solution()
array = [5,4,3,211,1]
print(sol.SelectionSort(array))
print(sol.SelectionSort(array))
print(sol.insertionSort(array))