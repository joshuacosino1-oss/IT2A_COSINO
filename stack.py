# Assessment 3.2 - Stack (LIFO)
# Based on Assessment 3.1: Push the letters of COSINO, then pop one at a time.

stack = []

for letter in "COSINO":
    stack.append(letter)

print("STACK (LIFO)")
print("Initial stack (bottom to top):", stack)

while len(stack) > 0:
    removed = stack.pop()
    print("Popped:", removed)
    print("Stack after pop:", stack if stack else "Empty")

print("Stack is now empty.")
