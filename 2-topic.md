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

```

<!-- Problem to Solve -->
## Problem to Solve: Improve Circular Linked Lists

You may have noticed with this singly-linked implementation that removing an item from the list takes O(n) time. Your challenge is to add take the Linked List from the example and turn it into a _doubly-linked_ list and implement the remove function (`pop()`) so that it has O(1) time complexity (so that it doesn't need to loop through the entire list).

<!-- Link to solution -->
You can check your code with the solution here: [Solution](tbd.py)

### [Back to Welcome Page](0-welcome.md)

[Previous](1-topic.md)

[Next](3-topic.md)
