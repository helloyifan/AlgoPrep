# Tried for 30 mins, got confused, but didnt get it, will try later

from typing import List


# General idea, keep track of the number of ones that are oppen
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rets = []
        rets.append('(')
        
        for i in range(0, n):
            tempRets = []
            while len(rets) > 0:
                cur = rets.pop()

                if (self.countOpening(cur) < n - i):
                    tempRets.append(cur + '(')

                if (self.countOpening(cur) > 0):
                    tempRets.append(cur + ')')
            rets = tempRets
        return rets


    def countOpening(self, string):
        open = string.count('(')
        close = string.count(')')
        return open - close

    #def helper(self, rets, opens, remaining):



if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(1))
    # ()
    print(sol.generateParenthesis(2))
    # ()() (())    
