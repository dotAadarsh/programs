# Circular Queue Implementation

class myCircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element in circular queue
    def enqueue(self, data):
        
        if ((self.tail + 1) % self.k == self.head):
            print("The circularqueue isfull\n")
        
        elif(self.head == -1):
            self.head = 0
            self.queue = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data 

    # Delete an element from the circular queue
    def dequeue(self):
        if(self.head == -1):
            print("Circular queue is empty\n")
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    # Print the queue
    def printQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end= " ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end = " ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end = " ")
            print()

q = myCircularQueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print("Initialqueue")
q.printQueue()

q.dequeue()
print("After removing an element")
q.printQueue()