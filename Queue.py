class Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if(self.is_empty()):
            return None
        self.queue.pop(0)
        
    def is_empty(self):
        return len(self.queue)==0
    def print_queue(self):
        return str(self.queue)
        


queue = Queue()
print("Enter the elements to append into queue")
vals = list(map(int,input().split()))

for val in vals:
    queue.enqueue(val)
queue.enqueue(34)
print(queue.print_queue())
queue.dequeue()
print(queue.print_queue())
print(f"is queue empty:{queue.is_empty()}")
