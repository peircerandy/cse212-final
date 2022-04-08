# Trees

<!-- Introduction -->
## Introduction

Trees are a data type? Yep! Just think about it. A tree starts with its trunk, then splitting of from the  truck are its branches, there could just be one, two or many branches splitting from the trunk, then each branch in turn can also have a few or many branches splitting from them until, and this continues for branch off of a branch until we finally have a small branch called a **leaf** that has no branches. Each branch can contain a little information on it and then it directs you to the branches that split from it. A well known example of the tree data structure would be a family tree. Your ancestors are closer to the trunk of the tree, their children are branches off of them, their children each have children branching off from them, until it gets to your parents and then you. If you don't have any kids then that makes you a _leaf_.

<!-- Common uses -->
## Common Uses

- Decision trees. Each each branch represents a different decision that could be made with certain decisions leading to different future decisions.Often used in Artificial intelligence programs such as video game NPCs. 
- File Systems. On Windows the C drive is the **root** node (first node in the tree) and each file is a **child**, or branch of it.
- Binary Search Trees (BST). Used to quickly find, insert, and delete sorted data. It is much faster to find a data item from a BST than from a linked list because it doesn't have to traverse through each item. This tutorial will be going into a little bit more detail on binary trees.

<!-- Operations -->
## Operations and Performance of BSTs

Trees are very similar to [linked lists](2-topic.md). Trees, like liked lists, also use **nodes** to represent data. Each node contains a variable  for the data, a variable that links to its **parent** node (the node it branches from), and a variable with a link for each of its branches/children. Binary Search Trees have two children, and left child where items of lesser value than the parent node are are stored, and a right child where items of greater value than the parent node are stored.

Binary Search Trees typically have functions with the following functions:

- `insert(value)` -- This operation searches for the correct location for the data based on its value. As it searches each layer for the appropriate spot the the amount of nodes it needs to search close to halved each time it searches a new layer as it chooses to look down either the left **subtree** (tree formed by selecting a different node as a root and including all of its children) or right subtree based on the value. Because of this nature of BSTs this operation takes O(log n) time.
- `remove(value)`-- This operation works much the same as inserting, also taking O(log n) complexity, except instead of looking for an empty spot it is looking for a node that contains the value and it also requires re-parenting the children of the removed node to the parents of that node.
- `contains(value)` -- Again, this works much the same as the previous two operations, retuning `True` if it finds the value and is O(log n)
- Traversing functions that return the all the values in the BST in the order of their value. Since these functions have to visit each node they take O(n) time.
- Height getting functions that return the maximum number of layers of a subtree formed from a given node, this takes o(n) time.

> Note:
> It is also often useful to us balancing algorithms to for a **Balanced Binary Search Tree**. A BST is **Balanced** if the subtrees at each layer have the same height with a variance of 1 for the layers that include leaves. If a tree is not balanced then it is possible to lose much of the O(log n) performance advantage that trees have. For example, if items where added to a BST in a descending order of value then each new item would just be added as the left child of the previously added one, making a very lopsided tree that isn't much different from a linked list. Adelson-Velskii and Landis Tree or AVL is a common algorithm for balanced binary search trees.

<!-- Example -->
## Example: Making a BST

The following code is an example of how a Binary Search Tree could be implemented. This example does not show a Balanced Binary Search Tree so it is vulnerable to becoming lopsided, especially if remove is used a lot.

> Note  
> Because many of the operations on BSTs are repetitive actions that can also be done on the subtrees, it is very useful to use recursion in the implementation of these functions. Recursion is when a function calls itself, passing in a value that is updated with each call to iterate the operation forward until some base case is met.

``` python

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
        
# Test Cases:
tree = BST()
print(tree.contains(5)) # False
print(tree.height()) # 0
tree.insert(5)
print(tree.root.data) # 5
print(tree.height()) # 1
tree.insert(3) 
print(tree.root.left.data) # 3
print(tree.contains(5)) # True
print(tree.contains(3)) # True
print(tree.contains(2)) #d False
print(tree) # Tree[3, 5]
tree.insert(2)
tree.insert(1)
tree.insert(6)
tree.insert(7)
print(tree) # BST[1, 2, 3, 5, 6, 7]
tree.remove(3)
print(tree) # BST[1, 2, 5, 6, 7]
tree.remove(7)
print(tree) # BST[1, 2, 5, 6]
print(tree.height()) # 3
```

#### [source code](exampleBST.py)

<!-- Problem to Solve -->
## Problem to Solve: Book Sort

You have a vast collection of books in your home library and you want to keep track of all of the titles you own. You frequently add new books to your collection or give books form your collection to others.

Download the [exampleBST.py](exampleBST.py) file that includes the implementation of the tree shown above. Include it in a new python program (using `from exampleBST import BST`) that uses the BST class to keep track of book titles. Create a simple interface to go with it as shown in the execution example.

> ### Hints
>
>- Use a while loop inside of `main()` to get input and display output
>- Create 4 functions in addition to `main()`
>
>   - `add_title()`: gets title from input and _inserts_ the title into the tree
>   - `remove_title()`: gets title from input and _removes_ the title from the tree
>   - `view_collection()`: shows a numbered list of each title in Alphabetical order
>     - since we are putting strings into the binary tree instead of numbers this is the method that the tree uses to sort and order the data
>   - `search_collection()`: gets title from input and searches the tree to see if it _contains_ the title

Example of execution:

``` terminal
r: remove title, v: view collection, 
s: search collection for title
Enter a command: v

No Books

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: a

Input Book Title: Huck Finn      

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: a

Input Book Title: Tom Sawyer

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: v

 Books:
1. Huck Finn
2. Tom Sawyer

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: s

Input Book Title: Tom Sawyer
Tom Sawyer is in your collection

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: s

Input Book Title: Tom
Tom is not in your collection

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: r

Input Book Title: Tom Sawyer

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: s

Input Book Title: Tom Sawyer
Tom Sawyer is not in your collection

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: v

 Books:
1. Huck Finn

Commands -- q: quit, a: add book title, 
r: remove title, v: view collection, 
s: search collection for title
Enter a command: q
```

<!-- Link to Solution -->
You can check your code with the solution here: [Solution](library.py)

### [Back to Welcome Page](0-welcome.md)

[Previous](2-topic.md)