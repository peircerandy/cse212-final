

class CircularLinkedList:
    
    class Node:
        
        def __init__(self, data):
            
            self.data = data
            self.next = None
            self.prev = None
        
    def __init__(self):
        
        self.tail = None
        
    def append(self, value):
        
        new_node = CircularLinkedList.Node(value)
        
        if self.tail is None:
            self.tail = new_node
            self.tail.next = self.tail
            self.tail.prev = self.tail
            
        else:
            new_node.next = self.tail.next
            self.tail.next.prev = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def pop(self, index = -1):
        
        if self.tail == None:
            return None
        if self.tail == self.tail.next:
                data = self.tail.data
                self.tail = None
                return data
        
        curr = self.tail
        if index < 0:
            for i in range(index, -1):
                curr = curr.prev
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            data = curr.data
            if curr == self.tail:
                self.tail = curr.prev
            return data
        else:
            for i in range(index):
                curr = curr.next
            data = curr.next.data
            curr.next = curr.next.next
            curr.next.next.prev = curr
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
cll = CircularLinkedList()
print(cll)
print(cll.pop())
cll.append(1)
print(cll)
print(cll.tail.data)
print(cll.tail.next.data)
print(cll.pop())
print(cll)
cll.append(1)
cll.append(2)
cll.append(5)
cll.append(3)
cll.append(-3)
cll.append(4)
print(cll)
print(cll.tail.data)
print(cll.tail.next.data)
print(cll.pop())
print(cll)
print(cll.tail.data)
print(cll.tail.next.data)
print(cll.pop(0))
print(cll)
print(cll.tail.data)
print(cll.tail.next.data)
print(cll.pop(5))
print(cll)
print(cll.tail.data)
print(cll.tail.next.data)
print(cll.pop(-4))
print(cll)
print(cll.tail.data)
print(cll.tail.next.data)
