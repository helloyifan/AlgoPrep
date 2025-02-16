from typing import List
from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debtDict = defaultdict(int)
        for t in transactions:
            fromId, toId, amount = t[0], t[1], t[2]

            debtDict[fromId] += amount
            debtDict[toId] -= amount
        
        # convert debtDict to debtList
        debtList = []
        for key in debtDict:
            debtList.append(debtDict[key])
        print(debtList)

        def dfs(k, remainingList):
            if k == len(remainingList):
                return 0

            if remainingList[k] == 0:
                return dfs(k+1, remainingList)

            head = remainingList[k]

            minVal = float('inf')
            for i in range(k+1, len(remainingList)): 
                cur = remainingList[i]
                if head*cur < 0:
                    remainingList[i] = cur + head

                    minVal = min(minVal, 1+ dfs(k + 1, remainingList))

                    remainingList[i] = cur # backtrack
                    
                    # if head + cur == 0:
                    #     break
            return minVal
        
        ret = dfs(0, debtList)
        print(ret)
        return ret
    
sol = Solution()
sol.minTransfers([[0,1,10],[2,0,5]]) # 2
sol.minTransfers([[0,1,10],[1,0,1],[1,2,5],[2,0,5]]) # 1
sol.minTransfers([[0,1,1],[1,2,1],[2,3,4],[3,4,5]])  # 3