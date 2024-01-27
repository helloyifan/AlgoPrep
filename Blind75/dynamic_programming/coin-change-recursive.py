# Spend 20 min and failed wrong way compeletly
# Spend another 30 mins: i got a solution that works but obvisouly since no DP it takes too long
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.dp = {} # amount: [...]
        self.coins = coins
        self.rets = []

        self.helper([], amount)

        minCoins = float('inf')
        for ret in self.rets:
            minCoins = min(minCoins, len(ret))

        if minCoins == float('inf'):
            return -1
        return minCoins

    def helper(self, coinsSoFar, amount):
        if amount == 0:
            sortedCoins = sorted(coinsSoFar)
            if not sortedCoins in self.rets:
                self.rets.append(sortedCoins)
            return 

        for coin in self.coins:
            remaining = amount - coin
            if remaining >= 0:
                coinsSoFarCopy = coinsSoFar[:]
                coinsSoFarCopy.append(coin)
                self.helper(coinsSoFarCopy, remaining)

        return 

if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1,2,5], 11))