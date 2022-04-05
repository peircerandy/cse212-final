from collections import deque

def addtask(tasks):
    task = input("\nWhat is the task? ")
    tasks.append(task)
    
def finishtask(tasks):
    if len(tasks) > 0:
        task = tasks.popleft()
        print(f"\nTask \"{task}\" finished.")

def showtasks(tasks):
    if (len(tasks) <= 0):
        print("\nNo Tasks")
        return
    print("\n Tasks:")
    num = 1
    for task in tasks:
        print(f"{num}. {task}")
        num +=1

def main():
    tasks = deque()
    command = None
    while(command != 'q'):
        print("Commands -- q: quit, s: see tasks, ")
        print("n: add new task, f: mark next task complete")
        command = input("Enter a command: ")
        if command == 's': 
                showtasks(tasks)
        if command == 'n': 
                addtask(tasks)
        if command == 'f': 
                finishtask(tasks)
        print()

main()