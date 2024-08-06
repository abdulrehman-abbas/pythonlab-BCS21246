class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if(self.isEmpty()):
            return "Empty Queue"
        else:
            return self.items.pop(0)
        
    def __str__(self):
        return str(self.items)
    

queue = Queue()

print(queue.dequeue())

queue.enqueue(10)
print(queue)

queue.enqueue(40)
queue.enqueue(60)
print(queue)

print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())

print(queue)
