# Solved in 15 mins from intuition
from typing import List
import copy
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phoneNumberToLetterMapping = {
            "2": "ABC",
            "3": "DEF",
            "4": "GHI",
            "5": "JKL",
            "6": "MNO",
            "7": "PQRS",
            "8": "TUV",
            "9": "WXYZ",
        }

        def helper(remainingDigits, output):
            if len(remainingDigits) == 0:
                if output == "":
                    return[]
                return [output.lower()]
            
            letters = phoneNumberToLetterMapping[remainingDigits[0]]
            ret = []
            for l in letters:
                tempOutputCopy = copy.copy(output)
                tempOutputCopy = tempOutputCopy + l # adding last letter 
                tempRet = helper(remainingDigits[1:], tempOutputCopy)
                ret = ret + tempRet

            return ret
        
        ret = helper(digits, "")
        return ret 

sol = Solution()
print(sol.letterCombinations("34"))
print(sol.letterCombinations(""))