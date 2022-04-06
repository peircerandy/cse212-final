

class CircularLinkedList:
    
    class Node:
        
        def __init__(self, data):
            
            self.data = data
            self.next = None
        
    def __init__(self):
        
        self.tail = None
        
    def append(self, value):
        
        new_node = CircularLinkedList.Node(value)
        
        if self.tail is None:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
    
    def pop(self):
        
        if self.tail is not None:
            self.tail = self.tail.next

            
    def __iter__(self):
        
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
cll.append(1)
cll.append(2)
cll.append(2)
cll.append(2)
cll.append(3)
print(cll)
print(cll.tail.data)
print(cll.tail.next.data)
cll.pop()
print(cll)
print(cll.tail.data)
print(cll.tail.next.data)