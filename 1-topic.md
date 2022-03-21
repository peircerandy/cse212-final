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
For the sake of this tutorial we will be using python to demonstrate using a queue. 

## Example:


<!-- Problem to Solve -->
## Problem to Solve: Task List
<!-- Link to solution -->
You can check your code with the solution here: [Solution](tbd.py)



[Back to Welcome Page](0-welcome.md)