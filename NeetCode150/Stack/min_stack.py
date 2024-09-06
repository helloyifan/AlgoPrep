# Took 15 mins, 
# Got confused on some logic
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Base case
        if len(self.minStack) == 0:
            self.minStack.append(val)
        # Val isnt smaller
        elif self.minStack[-1] <= val:
            self.minStack.append(self.minStack[-1])
        # Val is smalle
        elif self.minStack[-1] > val:
            self.minStack.append(val)

        return

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # return -3
    minStack.pop()
    print(minStack.top()) # return 0
    print(minStack.getMin()) # return -2