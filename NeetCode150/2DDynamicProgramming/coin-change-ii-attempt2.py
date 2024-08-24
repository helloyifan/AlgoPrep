from typing import List

# Solution based on a diagram

# 30- minute attempt based on inspirtaion from neetcode
# not even close
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ## setup 
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))] #amount+1 to acocunt for amount of 0
        amountToColIndex = self.amountToIndexMapping(amount)
        colToAmount = self.indexToAmountMapping(amountToColIndex)
        # set base case
        zeroCol = amountToColIndex[0]
        for i in range(len(dp)): 
            dp[i][zeroCol] = 1 # because there is one way to sum up to 0

        c = len(amountToColIndex)-2 # -2 to awoid counting the 0 column (and 0 index offset)
        while c >= 0:
            r = len(coins)-1 #-1 to account of 0 index offset
            while r >=0:
                rightOfCell = dp[r][c+1] if c+1 < len(dp[0]) else 0
                downOfCell = dp[r+1][c] if r+1 < len(dp) else 0
                cellVal = max(rightOfCell, downOfCell)
                
                curAmount = colToAmount[c]
                curCoin = coins[r]

                print(curAmount, curCoin)
                if (curAmount % curCoin == 0):
                    dp[r][c] = cellVal + 1

                r-=1
            c -= 1


        print(amountToColIndex)
        self.printDP(dp)
        return dp[0][0]
    
    def amountToIndexMapping(self, amount):
        mapping = {}
        indexCount = 0 
        for i in range(amount, -1, -1):
            mapping[i] = indexCount 
            indexCount += 1
        return mapping # amount:index 
    
    def indexToAmountMapping(self, amountToIndexMapping):
        return {value: key for key, value in amountToIndexMapping.items()}



    def printDP(self, l):
        for r in l:
            print(r)
if __name__ == "__main__":
    sol = Solution()
    #sol.change(4, [1,2,3])
    sol.change(5, [1,2,3])