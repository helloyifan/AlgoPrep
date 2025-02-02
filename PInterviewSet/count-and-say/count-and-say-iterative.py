from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        countAndSayStr = '1'

        for _ in range(n-1):
            curChar = None
            curCharOccurance = 0

            newCountAndSayStr = ''
            for i, e in enumerate(countAndSayStr):

                if curChar == None or e != curChar:
                    if curChar != None: #only include in answer if e has been set b4
                        newCountAndSayStr += str(curCharOccurance) + curChar
                    curChar = e
                    curCharOccurance = 1
                else: # e == curChat
                    curCharOccurance +=1
            # Dont forget to add answer at the end
            newCountAndSayStr += str(curCharOccurance) + curChar
            print(newCountAndSayStr)
            countAndSayStr = newCountAndSayStr

            # Don't forget to reset variables
            curChar = None
            curCharOccurance = 0

        return countAndSayStr

sol = Solution()
sol.countAndSay(4)
sol.countAndSay(1)
sol.countAndSay(30)
