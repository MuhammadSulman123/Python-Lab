# lab 4

# Stack Implementation in Python

class Stack:

    def __init__(self):
        self.stack = []

    # Push element into stack
    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    # Remove top element
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            item = self.stack.pop()
            print(item, "popped from stack")

    # Show top element
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Create stack
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Display stack
s.display()

# Show top element
s.peek()

# Remove top element
s.pop()

# Display stack again
s.display()


# search algorithms

'''
numbers = [45, 12, 90, 6, 38, 17, 77, 23, 84]

numbers.sort()

print("Sorted list:", numbers)

target = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Number found at index:", mid)
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Number not found")

'''

    # Implementation of Queue in Python
''''
class Queue:
    def __init__(self):
        self.items = []

    # Add an item to the queue
    def enqueue(self, item):
        self.items.append(item)
        print(item, "added to queue")

    # Remove an item from the queue
    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty")
        else:
            item = self.items.pop(0)
            print(item, "removed from queue")

    # Display the queue
    def display(self):
        print("Queue:", self.items)


# Create Queue
q = Queue()

# Add items
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Display queue
q.display()

# Remove item
q.dequeue()

# Display queue again
q.display() '''