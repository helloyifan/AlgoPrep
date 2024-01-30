
# Spend 20 min and failed wrong way compeletly
# Spend another 30 mins: i got a solution that works but obvisouly since no DP it takes too long
# Jan 30. Spent another hour, it works but the call stack is limiting larger test cases damn
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.dp = {} # amount: length
        self.coins = coins
        self.rets = []

        self.helper(amount)
        # print(self.dp)

        if amount not in self.dp or self.dp[amount] == float('inf'):
            return -1
        return self.dp[amount]

    def helper(self, amount):
        print(amount)
        if amount == 0:
            return 0 # We are passing back the length starting at length 0
        if amount in self.dp:
            return self.dp[amount]
        
        minRet = float('inf')
        for coin in self.coins:
            remaining = amount - coin
            if remaining >= 0:
                ret = self.helper(remaining)
                ret += 1
                minRet = min(minRet, ret)
                if amount not in self.dp or self.dp[amount] > ret:
                    self.dp[amount] = ret
        return minRet 
    
if __name__ == '__main__':
    s = Solution()
    # print(s.coinChange([1,2,5], 11))
    # print(s.coinChange([2], 3))
    # print(s.coinChange([1], 0))
    # print(s.coinChange([1], 1))
    # print(s.coinChange([1,2147483647], 2))
    print(s.coinChange([2,4,6,8,10,12,14,16,18,20,22,24], 9999)) # This solution is too slow for this
