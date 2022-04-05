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