Antrian=[]
class queue_restoran:
    def __init__(self):
        self.data=[]
    def enqueue(self, data):
        self.data.append(data)
    def dequeue():
        self.data.pop(0)
    def peek(self):
        return self.data[0]
    def size(self):
        return len(self.data)