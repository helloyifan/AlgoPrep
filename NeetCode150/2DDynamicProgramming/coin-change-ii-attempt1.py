from typing import List
from collections import defaultdict

# Brute force solution
# Recursive, added memoization
# Anecdote is BFS, howeverm, we dont pick coins less then the previous coin (so if u pick 3 you dont pick 2 or 1)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def helper(sum, prevCoin):
            if (sum, prevCoin) in memo:
                print("hit")
                return memo[(sum, prevCoin)]

            # Bases cases
            if sum == amount:
                return 1
            elif sum > amount:
                return 0
            
            curCombinations = 0
            for coin in coins:
                if coin >= prevCoin:
                    curCombinations += helper(sum+coin, coin)

            if sum in memo:
                raise("error, sum already in memo")

            memo[(sum, prevCoin)] = curCombinations
            return curCombinations

        ret = helper(0, 0)
        return ret 


if __name__ == "__main__":
    sol = Solution()
    sol.change(4, [1,2,3])
    sol.change(5, [1,2,3])