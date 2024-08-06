import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


pq = PriorityQueue()

pq.put("task1", 3)
pq.put("task2", 1)
pq.put("task3", 2)

while not pq.is_empty():
    task = pq.get()
    print(task)
