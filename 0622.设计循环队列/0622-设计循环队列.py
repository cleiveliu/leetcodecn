class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [0] * k
        self.used = 0
        self.len = k
        self.front = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.used < self.len:
            if self.used == 0:
                self.data[self.tail] = value
                self.used += 1
                return True
            else:
                self.tail = (self.tail + 1) % self.len
                self.data[self.tail] = value
                self.used += 1
                return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.used > 0:
            if self.used == 1:
                self.used -= 1
                return True
            else:
                self.front = (self.front + 1) % self.len
                self.used -= 1
                return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.used > 0:
            return self.data[self.front]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.used > 0:
            return self.data[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.used == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.used == self.len


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
