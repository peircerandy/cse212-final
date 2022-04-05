# Queues
<!--Introduction-->
Amusement parks are fun places to visit.They have fun rides and good food, but there is one thing amusement parks have that nobody likes: _the **lines**_. Maybe if you're fast and get to a ride just after the park opened, you can get there before anyone else and you won't have to wait very long. But, if you're not so lucky you will have to wait for everyone who got to the ride before you to have their turn before you can get on the ride. We could also call these lines `queues`.

<!-- Definitions -->
## Definition

Queues are an ordered sequence of entities or data items where the entities are added to one side, what we call the `back`, and removed from the other side, what we call the `front`. This process is typically referred to as the **First In, First Out** (`FIFO`) rule.

Other important terms to remember are `enqueue` and `dequeue`. **Enqueuing** is the name for the process of adding entities to the back of a queue and **Dequeuing** is the name for the process for removing entities from the front of the queue.

<!-- Common uses -->
## Common Uses

Queues have many practical uses:

- When your listening to your favorite music player such as Spotify the next song that plays comes from the **queue**, you can add a song to the **queue** (_enqueue_) and it will be played after all the other songs that have already been added, the next song to play will be the one added before all of the other songs.
- Managing a the use of resources on a system such as a CPU processing the first task that needed to use it first
- Web server traffic, handling the requests of the clients in order of the requests.

## Performance and implementation in Python

For the sake of this tutorial we will be using python to demonstrate using a queue. A queue could be implemented by using a list but, another simple way is to use the "deque" class from the "collections" module built into python. The main advantage to using the deque class over a list is that it with a list the dequeue operation takes O(n) time complexity while the deque function for dequeueing takes O(1) time complexity. This is accomplished using a [linked list](2-topic.md) instead of an array (list) to implement the queue.

To be able to use the deque class you must include it at the beginning of your python code:

```python
from collections import deque
```

Then it needs to be initialized:

``` python
# initialize with name queue
queue = deque()
```

To _enqueue_ -- O(1):

``` python
queue.append(item)
```

To _dequeue_ -- O(1):

``` python
item = queue.popleft()
```

<!-- Example -->
## Example: Repeat after me

```python
from collections import deque 

# This function implements the enqueue
def getwords(words):
  word = input("Say something: ")
  words.append(word)

# This function implements the dequeue
def repeat(words):
  print("Number of items in the queue:",len(words)) # neat function to use with queues
  numitems = int(input("Number of items to repeat? "))
  for i in range(numitems):
    if len(words) > 0: # Can't dequeue from and empty queue
      print(words.popleft())
  

def main():
  words = deque()
  print("Hello, I will repeat back everything you have said to me when you tell me to!")
  done = False
  while (not done):
    getwords(words) # enqueue
    if(input("repeat back? (y/n): ") == "y"):
        repeat(words) # dequeue
    if(input("Done? (y/n): ") == 'y'):
        done = True
          
main()          
```
Example Output

``` terminal
Hello, I will repeat back everything you have said to me when you tell me to!
Say something: hi
repeat back? (y/n): y
Number of items in the queue: 1
Number of items to repeat? 2
hi
Done? (y/n): n
Say something: Hello 
repeat back? (y/n): n
Done? (y/n): n
Say something: How
repeat back? (y/n): n
Done? (y/n): n
Say something: are
repeat back? (y/n): y
Number of items in the queue: 3
Number of items to repeat? 2
Hello
How
Done? (y/n): n
Say something: you
repeat back? (y/n): y
Number of items in the queue: 2
Number of items to repeat? 1
are
Done? (y/n): n
Say something: doing
repeat back? (y/n): y 
Number of items in the queue: 2
Number of items to repeat? 10
you
doing
Done? (y/n): y
```

###### [source code](exampleQ.py)

<!-- Problem to Solve -->
## Problem to Solve: Task List

While you are at work your boss comes by every once in while and gives you a new task to accomplish. Sometimes he gives you a new task before you've finished the old one and other times he gives you multiple tasks at a time. He expects you to complete each task in the order he gives them to you.

Create a python program that uses a queue to keep track of all of the tasks your boss gives you.

Example Execution:

``` terminal
Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

No Tasks

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: n

What is the task? Do nothin

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. Do nothin

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: n

What is the task? do something

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. Do nothin
2. do something

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: f

Task "Do nothin" finished.

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. do something

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: n

What is the task? Sort files

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: n

What is the task? read memo 

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. do something
2. Sort files
3. read memo

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: f

Task "do something" finished.

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. Sort files
2. read memo

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: clean office

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: n

What is the task? clean office

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. Sort files
2. read memo
3. clean office

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: f

Task "Sort files" finished.

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. read memo
2. clean office

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: f

Task "read memo" finished.

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: n

What is the task? take a break

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. clean office
2. take a break

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: f

Task "clean office" finished.

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

 Tasks:
1. take a break

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: f

Task "take a break" finished.

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: s

No Tasks

Commands -- q: quit, s: see tasks, 
n: add new task, f: mark next task complete
Enter a command: q
```

<!-- Link to solution -->
You can check your code with the solution here: [Solution](taskList.py)

### [Back to Welcome Page](0-welcome.md)

[Next](2-topic.md)
