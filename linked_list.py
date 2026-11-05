# Assessment 3.2 - Linked List
# Based on Assessment 3.1: Insert the letters of COSINO, then delete nodes one by one.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next

    def display(self):
        if self.head is None:
            return "Empty"

        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return " -> ".join(values)


linked_list = LinkedList()

for letter in "COSINO":
    linked_list.append(letter)

print("LINKED LIST")
print("Initial list:", linked_list.display())

while linked_list.head is not None:
    linked_list.delete_first()
    print("After deletion:", linked_list.display())

print("Linked list is now empty.")
