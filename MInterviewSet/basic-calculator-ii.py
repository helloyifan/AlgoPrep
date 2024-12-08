# Notes: Used a deque(stack) to keep track of add and sub tracks that we do on second pass
# A smarter way would be to do sum(stack) instead of the second while loop passand to keep track of subtraction of num*-1
# TC: O(n)
# SC: O(n) for stack

from collections import deque
import math
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        curI = 0
        stack = []

        while curI < len(s):
            if s[curI] == "+" or s[curI] == "-" or s[curI] == "*" or s[curI] == "/":
                stack.append(s[curI])
                curI += 1
            else:
                curNum, newIndex = self.findNumberAtIndex(s, curI)
                curI = newIndex

                if len(stack) == 0 or stack[-1] == "+" or stack[-1] == "-":
                    stack.append(curNum)
                elif stack[-1] == "*":
                    sign = stack.pop()
                    prevNumber = stack.pop()
                    stack.append(prevNumber*curNum)

                elif stack[-1] == "/": 
                    sign = stack.pop()
                    prevNumber = stack.pop()
                    stack.append(math.floor(prevNumber/curNum))
        
        stack = deque(stack)

        while len(stack) > 1:
            num = stack.popleft()
            sign = stack.popleft()
            prevNumber = stack.popleft()

            if sign == "+":
                stack.appendleft(num + prevNumber)
            elif sign == "-":
                stack.appendleft(num - prevNumber)

        print(stack)
        return stack[0]

    def findNumberAtIndex(self, s, i):
        curI = i
        while curI < len(s) and s[curI].isnumeric():
            curI += 1
        return int(s[i: curI]), curI#where the number ends
            

sol = Solution()
# print(sol.findNumberAtIndex('123', 0))
# print(sol.findNumberAtIndex('123', 1))
# print(sol.findNumberAtIndex('123#', 1))
# print(sol.calculate("3+2*2"))
# print(sol.calculate("3/2 "))
# print(sol.calculate(" 3+5 / 2 "))
# print(sol.calculate(" 3"))
print(sol.calculate("0-2147483647"))
print(sol.calculate("1-1+1"))