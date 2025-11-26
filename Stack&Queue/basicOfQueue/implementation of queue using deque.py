from collections import deque



class Queue:
    def __init__(self):
        self.queue=deque()

    

    def isempty(self):
        if self.queue is None:
            return True
        return False
    


    def enqueue(self,data):
        self.queue.append(data)

    
    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        ele=self.queue.popleft()
        return f"{ele} removed from queue"
    

    def peek(self):
        if self.isempty():
            return "Queue is empty"
        return self.queue[0]
    
    def rear(self):
        if self.isempty():
            return "Queue is empty"
        return self.queue[-1]
    

    def length(self):
        return len(self.queue)
    


