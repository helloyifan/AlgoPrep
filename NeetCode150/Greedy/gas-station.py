# Took 36min, of just coding and abusing the debugger bcuz im kinda stupid
# brute force solution
# Time Comp:
# O(n^2) range length and we interate length times
# Space Complexity 
# O(1)

# greey solution
# Time Comp:
# O(n) 
# Space Complexity 
# O(1)
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
        if sum(gas) < sum(cost):
            print(-1)
            return -1

        total = 0
        ret = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            # If total is <0 then it doesnt work 
            # We ran out of gas
            # We are being greedy so
            # We presume the next spot is the starting spot
            if total < 0:
                # When the number is less then 0, we reset it to 0
                # because we update the starting point
                total = 0 
                
                ret = i + 1
        print(ret)
        return ret
        
sol = Solution()#
sol.canCompleteCircuit([1,2,3,4], [2,2,4,1]) # 3
sol.canCompleteCircuit([1,2,3], [2,3,2]) # -1


sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) # 3

# Stepping through the problem
# gas   1, 2, 3, 4
# cost  2, 2, 4, 1
# diff  -1, 0, -1, 3
# total:
#       -1, 0, -1, 3 
# 3 is the first point where the sum is greater then 0
# when the number is less then 0, we reset it to 0

# Answer is index 3

# gas    1,  2,  3, 4, 5
# cost   3,  4,  5, 1, 2
# diff  -2, -2, -2 ,3, 3
# total:
#       -2, -2, -2, 3, 6 


# answer is index 3
# From this test case, we observe that we need the 
# first point where the total sum is greater then 0
