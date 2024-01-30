## Notes:
'''
Notes from attempt 1 of bottom up:
# Round 1
1: [1]
2: [2]
5: [5]
# Round 2
2: [1,1] but since its more coins, dont use
3: [1,2]
6: [1,5]
3: [2,1] but since its the same as [1,2] we ignore (sort and dedup)
4: [2,2]
7: [2,5]
5: [5,1] but since its the same as [5,1] we ignore (sort)
# Round 3
Too lazy to write
'''

'''
Attempt 2finally passed
'''

# Looking back this was a pretty naive solution, using a dict and keeping track how many number of each would of been a better datastructure
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        dp = {}
        minVal = float('inf') #the minimum  value we can currently make (if it above target then theres no target)
        # Inital insert
        for coin in coins:
            dp[coin] = 1
            minVal = min(minVal, coin)

        # need a condition, when do we stop
        # we go until we have target, unless target is unachieveable
        while amount not in dp and minVal < amount:
            tempDp = {}
            minVal = float('inf') # Reset minVal

            for key, value in dp.items():
                for coin in coins:
                    newKey = key + coin
                    newValue = value + 1
                    if newKey in dp and dp[key] < newValue:
                        continue

                    minVal = min(minVal, newKey)
                    tempDp[newKey] = newValue
            dp = tempDp.copy()
        
        if amount in dp:
            return dp[amount]
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1,2,5], 11))
    print(s.coinChange([2], 3))
    print(s.coinChange([1], 0))
    print(s.coinChange([1], 1))
    print(s.coinChange([1,2147483647], 2))
    print(s.coinChange([2,4,6,8,10,12,14,16,18,20,22,24], 9999)) # This solution is too slow for this
