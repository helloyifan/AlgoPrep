## Notes:
'''
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
        minKey = float('inf')
        # Initial setup
        for coin in coins:
            dp[coin] = [coin]
            minKey = min(minKey, coin)


        while (amount not in dp) and minKey < amount: # How do we know when to stop 
            print(minKey)
            print(dp)
            minKey = float('inf') # Reset the minKey (to be max val) so we can figure the lowest amount of coins after getting 1 of every new coin
            newDp = {}
            for key, value in dp.items():
                for coin in coins:
                    newKey = key + coin
                    minKey = min(minKey, newKey)

                    # Less efficient to make this but not use it always
                    newValue = value[:]
                    newValue.append(coin)

                    if newKey in newDp:
                        continue

                    elif newKey in dp:
                        if len(dp[newKey]) > len(newValue):
                            newDp[newKey] = newValue
                        else:
                            newDp[newKey] = dp[newKey]

                    elif newKey in newDp:
                        if len(newDp[newKey]) > len(newValue):
                            newDp[newKey] = newValue
                
                    else: # newKey not in newDp:
                        newDp[newKey] = newValue
                        if newKey == amount:
                            break


            dp = newDp
            # print(dp)

        if amount in dp:
            return len(dp[amount])
        return -1

if __name__ == '__main__':
    s = Solution()
    # print(s.coinChange([1,2,5], 11))
    # print(s.coinChange([2], 3))
    # print(s.coinChange([1], 0))
    # print(s.coinChange([1], 1))
    # print(s.coinChange([1,2147483647], 2))
    print(s.coinChange([2,4,6,8,10,12,14,16,18,20,22,24], 9999)) # This solution is too slow for this

    
    