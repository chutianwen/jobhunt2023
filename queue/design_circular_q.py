# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".
#
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
#
# Implementation the MyCircularQueue class:

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.first = None
        self.last = None

    def enQueue(self, value: int) -> bool:
        if self.cap > 0:
            if not self.first:
                self.first = self.last = Node(value)
            else:
                self.last.next = Node(value)
                self.last = self.last.next
            self.cap -= 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.first:
            self.first = self.first.next
            self.cap += 1
            if self.first is None:
                self.last = None
            return True
        else:
            return False

    def Front(self) -> int:
        if self.first:
            return self.first.val
        else:
            return -1

    def Rear(self) -> int:
        if self.last:
            return self.last.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.first is None

    def isFull(self) -> bool:
        return self.cap == 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


class MyCircularQueue2:

    def __init__(self, k: int):
        self.cap = k
        self.budget = k
        self.data = [0] * k
        self.first = self.last = None

    def enQueue(self, value: int) -> bool:

        if self.budget > 0:
            if self.first is None:
                self.first = self.last = 0
            else:
                self.last = (self.last + 1) % self.cap

            self.data[self.last] = value
            self.budget -= 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            # one item only
            if self.first is not None and self.first == self.last:
                self.first = self.last = None
            else:
                self.first = (self.first + 1) % self.cap
            self.budget += 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[self.first]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[self.last]

    def isEmpty(self) -> bool:
        return self.budget == self.cap

    def isFull(self) -> bool:
        return self.budget == 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()