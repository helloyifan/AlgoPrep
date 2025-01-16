# Notes: Recursion is fun, nothing specical. took under 10 mins
# TC: O(2^n) since we iteratte throgh every character, we will be doing 2^n recursive calls in final iteration
# SC: O(2^n) in total: for call stack we use O(n), however the String we  are building will be 2^n size

from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        
        def recusriveLSE(s, n):
            if n == 0:
                return s
            
            curS  = ''

            prevChar = ''
            prevCount = 0
            for i, e in enumerate(s):

                if e != prevChar:
                    # Write old to array
                    if prevChar != '':
                        curS +=  str(prevCount) + prevChar
                    # update prev tracker
                    prevChar = e
                    prevCount = 0
                prevCount += 1
            # Add remaining 
            curS +=  str(prevCount) + prevChar


            # TODO add recurions
            return recusriveLSE(curS, n-1)

        ret = recusriveLSE('1', n-1)
        print(ret)
        return ret

sol = Solution()
sol.countAndSay(4)
sol.countAndSay(1)
sol.countAndSay(30)
