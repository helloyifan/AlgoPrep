class MinStack:

    def __init__(self):
        self.stack =  []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if (len(self.minStack) == 0 or self.minStack[-1] > val):
            self.minStack.append(val)
        else:
            prevMin = self.minStack[-1]
            self.minStack.append(prevMin)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if (len(self.stack) == 0):
            return None
        return self.stack[-1]   

    def getMin(self) -> int:
        if (len(self.minStack) == 0):
            return None
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()