

class CircularLinkedList:
    
    class Node:
        
        def __init__(self, data):
            
            self.data = data
            self.next = None # pointer to the next  value
            self.prev = None# pointer to the previous  value
        
    def __init__(self):
        
        self.tail = None
        
    def append(self, value):
        
        new_node = CircularLinkedList.Node(value)
        
        if self.tail is None: # empty list
            self.tail = new_node
            self.tail.next = self.tail
            self.tail.prev = self.tail
            
        else:
            self.tail.next.prev = new_node
            new_node.next = self.tail.next
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def pop(self, index = -1):
        
        if self.tail == None: # empty list
            return None
        if self.tail == self.tail.next:
                data = self.tail.data
                self.tail = None
                return data
        
        curr = self.tail
        if index < 0:
            # now that we do have a pointer to the previous node
            # removing the tail is O(1)
            for i in range(index, -1): # index = -1 = tail skips this loop
                curr = curr.prev
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            data = curr.data
            if curr == self.tail:
                self.tail = curr.prev
            return data
        else:
            # removing the head is actually O(1) since we start 
            # with access to is's previous node
            curr = self.tail.next
            for i in range(index): # index = 0 = head skips this loop
                curr = curr.next
            if curr == self.tail:
                self.tail = curr.prev
            data = curr.data
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            return data
            return data
        
            
    def __iter__(self):
        
        if self.tail == None:
            return
        
        curr = self.tail.next
        while True:
            yield curr.data 
            curr = curr.next
            if curr == self.tail.next:
                break
            
    def __str__(self) -> str:
        
        output = "CircularLinkedList["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
            
            
# Sample Tests
print("======pop from Empty list======")
cll = CircularLinkedList()
print(cll)
print(cll.pop()) # None
print("======append and pop from Single item list======")
cll.append(1)
print(cll)
print(cll.tail.data) # 1
print(cll.tail.next.data) # 1
print(cll.pop()) # 1
print(cll)
print("======append======")
cll.append(1)
cll.append(2)
cll.append(5)
cll.append(3)
cll.append(-3)
cll.append(4)
print(cll)
print(cll.tail.data) # 4
print(cll.tail.next.data) # 1
print("======Test remove tail -- pop()======")
print(cll.pop()) # 4
print(cll)
print(cll.tail.data) # -3
print(cll.tail.next.data) # 1
print("======Test remove head -- pop(0)======")
print(cll.pop(0)) # 1
print(cll)
print(cll.tail.data) # -3
print(cll.tail.next.data) # 2
print("======Test Circle remove -- pop(5)======")
print(cll.pop(5)) # 5
print(cll)
print(cll.tail.data) # -3
print(cll.tail.next.data) # 2
print("======Test  remove from middle -- pop(1)======")
print(cll.pop(1)) # 3
print(cll)
print(cll.tail.data) # -3
print(cll.tail.next.data) # 2
print("======Test remove tail method 2 -- pop(1)======")
print(cll.pop(1)) # -3
print(cll)
print(cll.tail.data) # 2
print(cll.tail.next.data) # 2

# doubly-linked sample tests
print("======Test more appends======")
cll.append(6)
cll.append(7)
cll.append(8)
print(cll)
print(cll.tail.data) # 8
print(cll.tail.next.data) # 2
print("======Test backwards remove from middle -- pop(-3)======")
print(cll.pop(-3)) # 6
print(cll)
print(cll.tail.data) # 8
print(cll.tail.next.data) # 2
print("======Test remove tail method 3 -- pop(-4)======")
print(cll.pop(-4)) # 8
print(cll)
print(cll.tail.data) # 7
print(cll.tail.next.data) # 2
print("======Test remove head method 2 -- pop(-2)======")
print(cll.pop(-2)) # 2
print(cll)
print(cll.tail.data) # 7
print(cll.tail.next.data) # 7
