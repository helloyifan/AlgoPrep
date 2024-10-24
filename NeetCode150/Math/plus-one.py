from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver = None
        for i in range(len(digits)-1, -1, -1):
            if carryOver == None or carryOver == True:
                if digits[i] == 9:
                    digits[i] = 0
                    carryOver = True
                else:
                    digits[i] += 1
                    carryOver = False
        
        if carryOver == True:
            digits.insert(0, 1)
        return digits
    
sol = Solution()
#print(sol.plusOne([1,2,3,4]))
#print(sol.plusOne([9,9,9]))
print(sol.plusOne([1,1,9,9,9]))
