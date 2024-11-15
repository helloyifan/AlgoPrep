from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ph = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ret = []
        for d in digits:
            if len(ret) == 0:
                ret  = [*ph[d]]
            else:
                tempRet = []
                for element in ret:
                    for letter in ph[d]:
                        tempRet.append(element + letter)
                ret = tempRet
        print(ret)
        return ret
sol = Solution()
sol.letterCombinations("23")
sol.letterCombinations("")
sol.letterCombinations("2")