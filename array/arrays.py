class Myarray:
    def __init__(self):
        self.length = 0 
        self.data = []

    def get(self, index):
        return self.data[index]
    
    def push(self, input):
        self.data.append(input)
        self.length += 1
        return self.data
    
    def pop(self):
        if self.length == 0:
            return "Array is empty"
        
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    
    def delete(self, index):
        item = self.data[index]
        self.ShiftItems(index)
        return item
    
    def ShiftItems(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


arr = Myarray()

# Test push
print("Push Test:", arr.push("apple"))  
print("Push Test:", arr.push("banana")) 

# Test get
print("Get Test (index 0):", arr.get(0)) 
print("Get Test (index 1):", arr.get(1)) 

# Test pop
print("Pop Test:", arr.pop()) 
print("After Pop:", arr.data)  


print("Delete Test (index 0):", arr.delete(0))  
print("After Delete:", arr.data)  
