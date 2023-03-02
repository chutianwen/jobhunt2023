class MyCircularDeque:

    def __init__(self, k: int):
        self.budget = self.cap = k
        self.front = self.last = -1
        self.data = [0] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.front == self.last == -1:
                self.front = self.last = 0
            else:
                self.front = (self.front - 1) % self.cap if self.front > 0 else self.cap - 1
            self.data[self.front] = value
            self.budget -= 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.front == self.last == -1:
                self.front = self.last = 0
            else:
                self.last = (self.last + 1) % self.cap
            self.data[self.last] = value
            self.budget -= 1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.last:
                self.front = self.last = -1
            else:
                self.front = (self.front + 1) % self.cap
            self.budget += 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.last:
                self.front = self.last = -1
            else:
                self.last = (self.last - 1) % self.cap if self.last > 0 else self.cap - 1
            self.budget += 1
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[self.last]

    def isEmpty(self) -> bool:
        return self.budget == self.cap

    def isFull(self) -> bool:
        return self.budget == 0

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()