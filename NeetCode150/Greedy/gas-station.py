# Took 36min, of just coding and abusing the debugger bcuz im kinda stupid
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        retIndex = -1
        for i in range(length):
            resultFlag = False

            # Attempt i
            curIndex = self.fetchOutOfRange(length, i)
            curGas = 0 
            startSpot = i
            endSpot = self.fetchOutOfRange(length, i + length -1)
            
            for j in range(startSpot, startSpot + length):
                curJ = self.fetchOutOfRange(length, j)

                # Adding gas as the next stop
                curGas += gas[curJ]

                curGas -= cost[curJ]
                if curGas < 0:
                    break

                # We got to the finish with gas
                if curJ == endSpot:
                    resultFlag = True

            if resultFlag == True:
                retIndex = i
                break
        
        print(retIndex)
        return retIndex

    def fetchOutOfRange(self, length, index):
        if index >= length:
            index -= length
        return index
    
sol = Solution()#
sol.canCompleteCircuit([1,2,3,4], [2,2,4,1]) # 3
sol.canCompleteCircuit([1,2,3], [2,3,2]) # -1
