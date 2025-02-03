# Notes: Airplane bottom up solution
# Code looks weird, but the idea is we count from 1 to amount (i val)
# and see whats the lowest number of coins we need to build each i 
# the thinking is 0 takes 0 coins, and each coin value takes 1 coin

# TC: O(amount*num_of_coincs): For each amount, we check all the coins we have, 
# SC: O(amount): We store something for each amount val
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0 # Base case
        for i in range(1, amount+1):
            
            set = False
            for coin in coins:
                curTarget = i - coin
                if curTarget in dp and dp[curTarget] != -1:
                    if i in dp:
                        dp[i] = min(dp[i], dp[curTarget] + 1)
                    else:
                        dp[i] = dp[curTarget] + 1
                    set = True

            if set == False:
                dp[i] = -1
        print(dp)
        return dp[amount]

s = Solution()
# print(s.coinChange([1,2,5], 11))
# print(s.coinChange([1,2,5], 13))
# print(s.coinChange([2], 3))
# print(s.coinChange([1], 0))
# print(s.coinChange([1], 1))
# print(s.coinChange([1,2147483647], 2))
# print(s.coinChange([2,4,6,8,10,12,14,16,18,20,22,24], 9999)) # This solution is too slow for this
# print(s.coinChange( [5, 12345, 6, 7,30], 35))
print(s.coinChange([2], 4))