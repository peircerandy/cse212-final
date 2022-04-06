
class Tree:
    
    class Node:
        
        def __init__(self, data):
            self.data = data 
            self.left = None
            self.right = None
            
    def __init__(self):
        self.root = None 
        
    def insert(self, data):
        
        new_node = Tree.Node(data)
        if self.root == None:
            self.root = new_node
        else:
            spotfound = False
            curr = self.root
            while not spotfound:
                if data <= curr.data:
                    if curr.left.data == None:
                        curr.left = new_node
                        spotfound = True
                    else:
                        curr = curr.left
                else:
                    if curr.right.data == None:
                        curr.right = curr
                        spotfound = True
                    else:
                        curr == curr.right
                        
    def contains(self, data):
        if self.root == None:
            return False
        else:
            spotfound = False
            curr = self.root
            while not spotfound:
                if data <= curr.data:
                    if curr.left.data == data:
                        return True
                    else:
                        curr = curr.left
                else:
                    if curr.right.data == None:
                        return True
                    else:
                        curr == curr.right
                        