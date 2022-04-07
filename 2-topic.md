# Linked Lists

<!-- Introduction -->
## Introduction

Typically, in programming, when we think about list we think about arrays. In many programming languages arrays are limited to only be able to hold the amount of items that they are initialized to with unless you implement a dynamic array. Python arrays are already implemented as dynamic arrays and are virtually unlimited in their capacity, but they have their disadvantages. The dynamic array has allocated pace in the computer's memory and whenever an item is added to the array that causes the array to exceed it's allocated memory it creates a new array with twice as much space allocated, copies over all the data from the precious array and adds the new item. Not only could this make an operation that takes O(1) time (if you were added to the end of the array) take O(n) time, it also takes up a lot of memory that may not ever be used.

Liked Lists are another form of lists that solve some of these problems. In a linked list data is stored into an object called a **node**. In addition to the data, each node also contains pointers or a _link_ to the next item in the list. If there is no next item then the link is empty (= None in python). Nodes are only created when more data is added to the list and nodes are removed if the data is removed, so there is only as many nodes as there are data items, thus we only use up as much memory as necessary --solving one of the problems with dynamic arrays. For example if the list only contains one item, then there will only be one node that will contain the data and an empty link. Linked Lists can also be **doubly-linked** and have a variable that contains a link to the previous node in the list as well as the next node. 

<!-- Common uses -->
## Common Uses

- Any application that has previous and next buttons such as those for traversing remembering your browser history or on a media player
- Crating a variable type, such ans an integer with infinite size
- Implementing queues and stacks.

<!-- Using a Linked list / Operations / performance -->
## Implementation and Performance in Python

If you followed my tutorial on [Queues](1-topic.md) then you might remember that the "deque" python class we used to implement a queue is a linked list. Well, since that class is a linked list it actually allows us to use it as one.

Since the data for a linked lists can only be accessed by links from neighboring nodes pointers to the **head** (first node in the list) and **tail** (last node in the list) are saved as the means for accessing the rest of the nodes, so there is typically functions to access them. With the `deque` class these are (using `list` for the name of initialized `deque` object) `list.appendleft(value)`and `list.append(value)` for inserting data at the head or the tail respectively, each with O(1) time complexity; `list.popleft()` and `list.pop()` for removing data (nodes) from the head or tail respectively, also typically with 0(1) time complexity. Linked lists can also have functions for getting, adding or removing data from the middle of the Linked lists such as `del list[i]`, but these operations take O(n) time complexity, so if they are used frequently then it would be better to use a dynamic array instead of a linked list.

<!-- Example -->
## Example: Making a Circular  Linked list

For a better understanding of how linked lists work here is and example of an implementation of a singly-linked Circular Linked list. Instead of having the _next_ pointer of the tail link to nothing it is linked to the first item in the list. Because of this we no longer need a pointer to the head because it can be accessed as the next node of the tail. This type of linked list is useful when the data needs to be accessed repeatedly in the same order.

``` python


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

```
##### [source code](2-topic-example.py)

<!-- Problem to Solve -->
## Problem to Solve: Improve Circular Linked Lists

You may have noticed with this singly-linked implementation that removing an item from the end of the list takes O(n) time when I said earlier that that takes O(1). With this implementation that is only possible with a doubly-linked list. Your challenge is to take the Linked List from the example and turn it into a _doubly-linked_ list and to update the remove function (`pop()`) so that it has O(1) time complexity when removing the tail (it doesn't need to go through a loop). Also add into the `pop()` function the ability to remove negative indexes from the list just as you can remove positive indexes (with the absolute value of some indexes greater than the number of items in the list).

Here is what the output of some possible test cases could look like:

``` terminal
======pop from Empty list======
CircularLinkedList[]
None
======append and pop from Single item list======
CircularLinkedList[1]
1
1
1
CircularLinkedList[]
======append======
CircularLinkedList[1, 2, 5, 3, -3, 4]
4
1
======Test remove tail -- pop()======
4
CircularLinkedList[1, 2, 5, 3, -3]
-3
1
======Test remove head -- pop(0)======
1
CircularLinkedList[2, 5, 3, -3]
-3
2
======Test Circle remove -- pop(5)======
5
CircularLinkedList[2, 3, -3]
-3
2
======Test  remove from middle -- pop(1)======
3
CircularLinkedList[2, -3]
-3
2
======Test remove tail method 2 -- pop(1)======
-3
CircularLinkedList[2]
2
2
======Test more appends======
CircularLinkedList[2, 6, 7, 8]
8
2
======Test backwards remove from middle -- pop(-3)======
6
CircularLinkedList[2, 7, 8]
8
2
======Test remove tail method 3 -- pop(-4)======
8
CircularLinkedList[2, 7]
7
2
======Test remove head method 2 -- pop(-2)======
2
CircularLinkedList[7]
7
7
```

> Hints  
>
> - Removing the head is already an O(1) operation, so removing the tail and removing negative integers can be implemented in much the same way, but with different starting and ending positions for the for loop, and by iterating to the previous node instead of the next one.
> - You will also need to update the constructor method (`__init__`) for the node class as well as the `append` method to support a pointer to the previous node.
>

<!-- Link to solution -->
You can check your code with the solution here: [Solution](2-topic-problem.py)

### [Back to Welcome Page](0-welcome.md)

[Previous](1-topic.md)

[Next](3-topic.md)
