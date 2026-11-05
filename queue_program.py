# Assessment 3.2 - Queue (FIFO)
# Based on Assessment 3.1: Enqueue the letters of COSINO, then dequeue one at a time.

from collections import deque

queue = deque()

for letter in "COSINO":
    queue.append(letter)

print("QUEUE (FIFO)")
print("Initial queue (front to rear):", list(queue))

while len(queue) > 0:
    removed = queue.popleft()
    print("Dequeued:", removed)
    print("Queue after dequeue:", list(queue) if queue else "Empty")

print("Queue is now empty.")
