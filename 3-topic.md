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

The following code is an example of how a Binary Search Tree could be implemented. This example does not show a Balanced Binary Search Tree so it is vulnerable to becoming lopsided.

> Note  
> Because many of the operations on BSTs are repetitive actions that can also be done on the subtrees, it is very useful to use recursion in the implementation of these functions. Recursion is when a function calls itself, passing in a value that is updated with each call to iterate the operation forward until some base case is met.

``` python

```

<!-- Problem to Solve -->
## Problem to Solve: Book Sort

<!-- Link to Solution -->
You can check your code with the solution here: [Solution](tbd.py)

### [Back to Welcome Page](0-welcome.md)

[Previous](2-topic.md)