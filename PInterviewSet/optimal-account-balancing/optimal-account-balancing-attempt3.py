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

        def dfs(remainingList):
            if len(remainingList) == 0:
                return 

            head = remainingList[0]
            for i in range(1, len(remainingList)): 
                cur = remainingList[1]

                if head*cur < 0:
                    


            return
        return
    
sol = Solution()
sol.minTransfers([[0,1,10],[2,0,5]])
#sol.minTransfers([[0,1,10],[1,0,1],[1,2,5],[2,0,5]])