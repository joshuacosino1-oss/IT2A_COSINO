# Assessment 3.2 - Deque (Double-Ended Queue)
# Based on Assessment 3.1: Add the letters of COSINO at the rear,
# then remove one letter from the front at a time.

from collections import deque

double_ended_queue = deque()

for letter in "COSINO":
    double_ended_queue.append(letter)  # Add to the rear.

print("DEQUE")
print("Initial deque (front to rear):", list(double_ended_queue))

while len(double_ended_queue) > 0:
    removed = double_ended_queue.popleft()  # Remove from the front.
    print("Removed from front:", removed)
    print("Deque after removal:",
          list(double_ended_queue) if double_ended_queue else "Empty")

print("Deque is now empty.")
