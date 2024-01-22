# Couldn't focus well on this problem initally, tried solving with out two pointers but finished with 2 pointers
# took 10 mins when i was actually focused
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        h, t = 0 , 0
        maxProfit = prices[h] - prices[t]
        while h < len(prices):
            # move tail if val at head is less then val at tial
            if prices[h] < prices[t]:
                t = h
            maxProfit = max(maxProfit, prices[h] - prices[t])
            h += 1
        return maxProfit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))

    print(s.maxProfit([7,6,4,3,1]))

    print(s.maxProfit([7,6,4,3,1]))

