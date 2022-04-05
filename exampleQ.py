from collections import deque

words = deque()

print("Hello, I will repeat back everything you have said to me when you tell me to!")
done = False
while (not done):
    print("Say something: ")
    word = input()
    words.append(word)
    print("repeat back? (y/n): ")
    repeat = input()
    if(repeat == "y"):
        print("Number of items in the queue:",len(words))
        print("Number of items to repeat? ")
        numitems = int(input())
        for i in range(numitems):
          if len(words) > 0:
            print(words.popleft())
    print("Done? (y/n): ")
    if(input() == 'y'):
        done = True