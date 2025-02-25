from typing import List

class Solution:
    # dfs way
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        maxRet = float('-inf')
        def dfs(piles, alice, bob, front, end, aTurn):
            nonlocal maxRet

            if len(piles) == 0:
                maxRet = max(maxRet, alice)
                return

            if piles

            front = piles[0]
            back = piles[-1]
            
            pileWithOutFront = piles[1:]
            pileWithOutBack = piles[:len(piles)-1]

            if aTurn == 1:
                dfs(pileWithOutFront, alice+front, bob, aTurn*-1)
                dfs(pileWithOutBack, alice+back, bob, aTurn*-1)
            else:
                dfs(pileWithOutFront, alice, bob+front, aTurn*-1)
                dfs(pileWithOutBack, alice, bob+back, aTurn*-1)

        dfs(piles, 0, 0, 1) # 1 mean A's turn

        # post processing
        # if the most score A can get is bigger then half of piles, then A wins
        totalStones = 0
        for i in piles:
            totalStones += i


        aWins = False
        if maxRet > (totalStones/2):
            aWins = True
        print(aWins)
        return aWins
    


sol = Solution()
sol.stoneGame([5,3,4,5]) # True
sol.stoneGame([3,7,2,3]) # True