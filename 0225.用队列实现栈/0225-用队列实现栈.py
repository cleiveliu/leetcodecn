class Queue:
    def __init__(self):
        self.data = []

    def push_back(self, x):
        self.data.append(x)

    def pop_front(self):
        if self.data.__len__() > 0:
            return self.data.pop(0)

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.q1.empty():
            self.q2.push_back(x)
        else:
            self.q1.push_back(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1.empty() and self.q2.empty():
            return
        if self.q1.empty():
            for _ in range(self.q2.size() - 1):
                self.q1.push_back(self.q2.pop_front())
            return self.q2.pop_front()
        else:
            for _ in range(self.q1.size() - 1):
                self.q2.push_back(self.q1.pop_front())
            return self.q1.pop_front()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1.empty() and self.q2.empty():
            return
        if self.q1.empty():
            for _ in range(self.q2.size() - 1):
                self.q1.push_back(self.q2.pop_front())
            top = self.q2.pop_front()
            self.q1.push_back(top)
            return top
        else:
            for _ in range(self.q1.size() - 1):
                self.q2.push_back(self.q1.pop_front())
            top = self.q1.pop_front()
            self.q2.push_back(top)
            return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty() and self.q2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
