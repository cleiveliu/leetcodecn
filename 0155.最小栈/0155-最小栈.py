class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        self.mins = []

    def push(self, x: int) -> None:
        self.vals.append(x)
        if not self.mins:
            self.mins.append(x)
        else:
            self.mins.append(min(x, self.mins[-1]))

    def pop(self) -> None:
        if self.vals:
            self.vals.pop()
            self.mins.pop()

    def top(self) -> int:
        if self.vals:
            return self.vals[-1]

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
