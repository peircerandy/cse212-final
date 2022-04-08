from exampleBST import BST

def add_title(library):
    title = input("\nInput Book Title: ")
    library.insert(title)

def remove_title(library):
    title = input("\nInput Book Title: ")
    library.remove(title)
    
def view_collection(library):
    if library.height() <= 0:
        print("\nNo Books")
        return
    print("\n Books:")
    num = 1
    for title in library:
        print(f"{num}. {title}")
        num +=1
        
def search_collection(library):
    title = input("\nInput Book Title: ")
    if library.contains(title):
        print(f"{title} is in your collection")
    else:
        print(f"{title} is not in your collection")
        

def main():
    library = BST()
    
    command = None
    while(command != 'q'):
        print("Commands -- q: quit, a: add book title, ")
        print("r: remove title, v: view collection, ")
        print("s: search collection for title")
        command = input("Enter a command: ")
        if command == 'a':
            add_title(library)
        if command == 'r':
            remove_title(library)
        if command == 'v':
            view_collection(library)
        if command == 's':
            search_collection(library)
        
        print()

main()