class Queue:
    def __init__(self):
        self.queue=[]

    
    def __str__(self):
       return " <- ".join([str(i) for i in self.queue])



    

    def isempty(self):
        if self.queue ==[]:
            return True
        return False
    


    def enqueue(self,data):
        self.queue.append(data)



    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        ele=self.queue.pop(0)
        return f"{ele} is removed from queue"
    

    def peek(self):
        if self.isempty():
            return "Queue is empty"
        return self.queue[0]
    

    def rear(self):
        if self.isempty():
          return "Queue is empty"
        return self.queue[-1]
    

    def size(self):
        return len(self.queue)







