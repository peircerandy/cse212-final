from collections import deque

def addtask(queue):
    print("what is the task? ")
    task = input()
    queue.append(task)
    
def finishtask(queue):
    task = queue.popleft()
    print(f"Task \"{task}\" finished.")

def quiting(command):
    if command == 'quit' or \
        command == 'Quit'or \
        command == 'q'or \
        command =='Q' or \
        command == 'x' or \
        command == 'done' or \
        command == 'd' or \
        command == 'Done' or \
        command == 'D':
            return True
    else:
        return False

def main():
    tasks = deque()
    command = None
    while(not quiting(command)):
        print("Commands -- q: quit, s: see tasks, n: add new task, f: mark next task complete")
        print("Enter a command:")
        command = input()
        


main()