class Queue:
    def __init__(self):
        self.queue = []

    # Add element
    def enqueue(self, item):
        self.queue.append(item)
    
    # Remove element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    # Display
    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("Queue aftere removing an element")
q.display()
