
class BST:
    
    class Node:
        
        def __init__(self, data):
            
            self.data = data
            self.left = None
            self.right = None
        
    def __init__(self):
        
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = BST.Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, node):  
        if  value < node.data:
            if node.left is None:
                node.left = BST.Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(value)
            else:
                self._insert(value, node.right)
                
    def contains(self, value) -> bool:
        if self.root is None:
            return False
        else:
            return self._contains(value, self.root)
    
    def _contains(self, value, node) -> bool:
        if node.data == value:
            return True
        elif value < node.data:
            if node.left is  not None:
                return self._contains(value, node.left)
        else:
            if node.right is not None:
                return self._contains(value, node.right)
        return False
    
    def remove(self, value):
        if self.root is None:
            return
        else:
            self._remove(value, self.root)
             
    def _remove(self, value, node):
        if value < node.data:
            if node.left is not None:
                if node.left.data == value:
                    temp = node.left.right
                    node.left = node.left.left
                    for data in self.traverse_forward(temp):
                        self.insert(data)
                else:
                    self._remove(value, node.left)
        else:
            if node.right is not None:
                if node.right.data == value:
                    temp = node.right.left
                    node.right = node.right.right
                    for data in self.traverse_forward(temp):
                        self.insert(data)
                else:
                    self._remove(value, node.right)
                
    def __iter__(self):
        
        yield from self.traverse_forward(self.root)
        
    def traverse_forward(self, node):
        if  node is not None:
            yield from self.traverse_forward(node.left)
            yield node.data 
            yield from self.traverse_forward(node.right)
            
    def height(self):
        if self.root is None:
            return 0
        else:
            return self.getheight(self.root)
    
    def getheight(self, node):
        left_height = 0
        right_height = 0
        
        if node.left is not None:
            left_height = self.getheight(node.left)
        if node.right is not None:
            right_height= self.getheight(node.right)
            
        if left_height > right_height:
            return 1 + left_height
        else:
            return 1 + right_height
        
    def __str__(self):
        output = "BST["
        first = True 
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
        
