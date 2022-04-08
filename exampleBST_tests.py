from exampleBST import BST

def main():
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
    
main()