class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return self.size() == 0

myQueue= Queue()
myQueue.enqueue("Mon")
myQueue.enqueue("Tue")

print myQueue.size()
print (myQueue.dequeue())
print myQueue.size()

