# Took 21mins but im not sure if isolved it optimally
# in fact im sure i didnt
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [] # [{min, val}]
        # Maybe this can be sorted 

        for num in nums:
            dp.append({
                "min": num,
                "val": 1 
            })

            higestValObj = None
            for obj in dp:
                if obj['min'] < num:
                    if higestValObj == None or obj['val'] > higestValObj['val']:
                        higestValObj = obj
            
            if higestValObj != None:
                newObj = {
                    "min": num,
                    "val": higestValObj['val'] + 1
                }
                dp.append(newObj)

        finalRet = None
        for obj in dp:
            if finalRet == None or obj['val'] > finalRet['val']:
                finalRet = obj   

        return finalRet['val']
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(sol.lengthOfLIS([0,1,0,3,2,3]))
    print(sol.lengthOfLIS([7,7,7,7,7,7,7]))
