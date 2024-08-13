# Attempt 2 took 10 mins, not sure where inspiration came from
from typing import List


# General idea, keep track of the number of ones that are oppen
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        retStack = []

        stack = []
        stack.append( ["", 0, 0])

        for i in range(0, (n*2)+1): # This is weird, but it makes sens, *2 because we want a loop for each ( and ), +1 for ret building at end
            tempStack = []
            while len(stack) > 0:
                cur = stack.pop()

                if cur[1] <= n:
                    openList = [cur[0] + "(", cur[1]+1, cur[2]]
                    tempStack.append(openList)
    
                if cur[2] <= n and cur[2] < cur[1]:
                    closeList = [cur[0] + ")", cur[1], cur[2]+1]
                    tempStack.append(closeList)

                if cur[1] == n and cur[2]== n:
                    retStack.append(cur[0])

            #stack swap
            stack = tempStack

        return retStack
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(1))
    # ()
    print(sol.generateParenthesis(2))
    # ()() (())    
    print(sol.generateParenthesis(3))
    # ()() (())    
    print(sol.generateParenthesis(4))
    # ()() (())    
    print(sol.generateParenthesis(5))
    # ()() (())    
