# Took 36min, of just coding and abusing the debugger bcuz im kinda stupid
from typing import List
class Solution:
    
    def bruteForce(self, gas: List[int], cost: List[int]) -> int:
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

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return
        
sol = Solution()#
sol.canCompleteCircuit([1,2,3,4], [2,2,4,1]) # 3
sol.canCompleteCircuit([1,2,3], [2,3,2]) # -1


# Stepping through the problem
# Col 1 is cost, col 2 is gas

# 0, +1 = 1
# -2, +2 (cant dont have enough gas)
# -2, +3
# -4, +4

# 0, +2 = 2
# -2, +3 = 3 (just enough gas)
# -4, +4 (cat dont have enough gas)
# -1, +1 

# 0, +3 = 3
# -4, +4 (dont have enough gas)
# -1, +2
# -2, +2

# Edge case 2
# It impossible if it cost more then we get (that case we return -1)

# It will always be possible otherwise
# There is only one solution

# cost [4,1,2,3]
# gas [5,2,3,0]

#  0, +2 = 2
# -1, +3 = 4
# -2, 0 = 2
# -3 (dont have enough)

# 0, +5 = 5
# -4, +2 = 3
# -1, +3 = 5
# -2, 0 = 3
# -3, 5 = 5
# --------
# Writing it more logically
# +5, -4 = 1
# +2, -1 = 2
# +3, -2 = 3
# +0, -3 = 0


# It seems like if you start with the highest gas, you win, but thats not accurate
# its figuring out where your gas is less then 0