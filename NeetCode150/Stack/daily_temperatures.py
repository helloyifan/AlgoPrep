# Summary took 20 mins
# Learning is that im an idiot and idk what a stack is, (i thought you pop the front element off which is wrong)
# Intuition is stack and ret are different
# You ad dthe prev day to the stack
# everytime you check how many prev days you can pop off with the current temp

# Complexity Analysis
# Time Complexity: O(n) processs each temp twice, once you pop on, once you pop off
# Space Comeplxity: O(n) stack can contain one of everything, ret is the length of temp

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = [] #{temp , index}

        for i, temp in enumerate(temperatures):
            while (stack and temp > stack[-1][0]): # stack[0] Day that was prev added to stack at some point
                cur = stack.pop() # You pop the last element of the list
                daysHotter = i - cur[1] # current array index minus cur index
                ret[cur[1]] = daysHotter # Days that are never set are 0, which is expected
            stack.append([temp, i])
        return ret
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([30,38,30,36,35,40,28]))


# [40, 40, 40, 40, 40, 40, 28]
# [30, 38, 38, 38, 38, 40, 40]