# Took 45 min of bad concentation
# I thin its just a weird question i havnt practice enough on
# I was kinda weak at .append vs .extend, 
# I was also weak at knowing to build the result at the base case vs in the back track (it was base case btw, not sure if it has to be)
# I was able to solve with intuition

from typing import List
import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def helper(s, curList):
            # base case
            if len(s) == 0:
                return [curList]

            ret = [] # list of list of rets
            for i in range(1, len(s)+1):
                curString = s[0:i]

                if self.isPali(curString):
                    copyiedList = copy.deepcopy(curList)

                    remaingString = s[i:]
                    copyiedList.append(curString)
                    
                    curRet = helper(remaingString, copyiedList)

                    ret.extend(curRet)
            return ret

        curList = []
        listOfValidPalindromes = helper(s, curList)

        print(listOfValidPalindromes)
        return listOfValidPalindromes
    
    def isPali(self, s):
        f, b = 0, len(s)-1
        while(f < b):
            if (s[f] != s[b]):
                return False
            f += 1
            b -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    sol.partition('aab')
    sol.partition('a')


## From aab
# We have to check if 
# a Y 
# a b X
# a Y
# b Y


# aa Y
# b Y


