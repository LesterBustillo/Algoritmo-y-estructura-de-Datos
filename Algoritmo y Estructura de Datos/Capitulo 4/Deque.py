class Deque:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertLeft(self, item):
        if self.isFull():
            raise Exception('Deque esta lleno')
        self.front = (self.front - 1) % self.capacity
        self.items[self.front] = item
        self.size += 1

    def insertRight(self, item):
        if self.isFull():
            raise Exception('Deque esta lleno')
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def removeLeft(self):
        if self.isEmpty():
            raise Exception('Deque esta vacio')
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def removeRight(self):
        if self.isEmpty():
            raise Exception('Deque esta vacio')
        self.rear = (self.rear - 1) % self.capacity
        item = self.items[self.rear]
        self.size -= 1
        return item

    def peekLeft(self):
        if self.isEmpty():
            raise Exception('Deque esta vacio')
        return self.items[self.front]

    def peekRight(self):
        if self.isEmpty():
            raise Exception('Deque esta vacio')
        return self.items[(self.rear - 1) % self.capacity]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    
    