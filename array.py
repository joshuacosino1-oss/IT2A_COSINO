# Assessment 3.2 - Array
# Based on Assessment 3.1: Add the letters of COSINO, then remove them one by one.

letters = ["C", "O", "S", "I", "N", "O"]

print("ARRAY")
print("Initial array:", letters)

while len(letters) > 0:
    letters.pop(0)  # Remove the first letter, one at a time.
    print("After removal:", letters if letters else "Empty")

print("Array is now empty.")
