# Linked Lists

<!-- Introduction -->
## Introduction
Typically, in programming, when we think about list we think about arrays. In many programming languages arrays are limited to only be able to hold the amount of items that they are initialized to with unless you implement a dynamic array. Python arrays are already implemented as dynamic arrays and are virtually unlimited in their capacity, but they have their disadvantages. The dynamic array has allocated pace in the computer's memory and whenever an item is added to the array that causes the array to exceed it's allocated memory it creates a new array with twice as much space allocated, copies over all the data from the precious array and adds the new item. Not only could this make an operation that takes O(1) time (if you were added to the end of the array) take O(n) time, it also takes up a lot of memory that may not ever be used. 

Liked Lists are another form of lists that solve some of these problems. In a linked list data is stored into an object called a **node**. In addition to the data, each node also contains pointers or a _link_ to the next item in the list. If there is no next item then the link is empty (= None in python). Nodes are only created when more data is added to the list and nodes are removed if the data is removed, so there is only as many nodes as there are data items, thus we only use up as much memory as necessary --solving one of the problems with dynamic arrays. For example if the list only contains one item, then there will only be one node that will contain the data and an empty link. Linked Lists can also be **doubly-linked** and have a variable that contains a link to the previous node in the list as well as the next node. 
 
<!-- Using a Linked list / Operations / performance -->
## Implementation and Performance in Python

<!-- Common uses -->
## Common Uses

<!-- Example --> 
## Example:

<!-- Problem to Solve -->
## Problem to Solve:

<!-- Link to solution -->
You can check your code with the solution here: [Solution](tbd.py)



[Back to Welcome Page](0-welcome.md)