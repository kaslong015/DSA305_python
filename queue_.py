class Queue:
    def __init__(self):
        self.size = 10
        self.que = []
        self.front = 0
     
    def display(self):
        pass

    def dequeue(self,value):
        if len(self.que) == 10:
            return "queue is full"
        else:
            self.que.append(value)


    
    def enqueue(self):
        if len(self.que) == 0:
            return "queue is empty"
        else:
            return self.que.pop(self.front)
           


    def _size(self):
        return len(self.que)




