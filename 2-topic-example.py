

class CircularLinkedList:
    
    class Node:
        
        def __init__(self, data):
            
            self.data = data
            self.next = None # pointer to the next  value
        
    def __init__(self):
        
        self.tail = None
        
    def append(self, value):
        
        new_node = CircularLinkedList.Node(value)
        
        if self.tail is None: # empty list
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
    
    def pop(self, index = -1):
        
        if self.tail == None: # empty list
            return None
        if self.tail == self.tail.next: # single item in the list
                data = self.tail.data
                self.tail = None
                return data
        
        if index < 0:
            curr = self.tail.next
            # since we don't have a pointer to the previous node we have to loop
            # through the entire list to change its "next" pointer so that it
            # no longer points to the removed tail.
            while True:
                if curr.next == self.tail:
                    curr.next = self.tail.next
                    data = self.tail.data
                    self.tail = curr
                    return data 
                else:
                    curr = curr.next
        else:
            curr = self.tail
            # removing the head is actually O(1) since we start 
            # with access to is's previous node
            for i in range(index): # index = 0 = head skips this loop
                curr = curr.next
            data = curr.next.data
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
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
