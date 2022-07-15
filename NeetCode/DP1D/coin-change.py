import enum
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Stupid edge case
        if (amount == 0):
            return 0

        dp = {}
        for i in range(1, amount +1):
            for coin in coins:
                if ((i - coin) in dp and dp[i-coin] != -1 ):
                    if (i in dp and dp[i] != -1):
                        dp[i] = min(dp[i-coin] + 1, dp[i])
                    else:
                        dp[i] = dp[i-coin] + 1 # maybe a better way to write this 
                elif(i == coin):
                    dp[i] = 1 # If the currnt i is equal to a coin, we have 1 coin
            

            if ( not i in dp):  #After trying all coins
                dp[i] = -1 #Impossible to make this value i

        print(dp)
        return dp[amount]

s = Solution()
coins = [1,2,5]
amount = 11
r = s.coinChange(coins, amount)
print(r)


coins2 = [2]
amount2 = 3
r2 = s.coinChange(coins2, amount2)
print(r2)

coins3 = [1]
amount3 = 0
r3 = s.coinChange(coins3, amount3)
print(r3)

coins4 = [5, 12345, 6, 7,30]
amount4 = 35
r4 = s.coinChange(coins4, amount4)
print(r4)

coins5 = [5, 12345, 6, 7,30]
amount5 = 19
r5 = s.coinChange(coins5, amount5)
print(r5)


# Notes

'''





'''