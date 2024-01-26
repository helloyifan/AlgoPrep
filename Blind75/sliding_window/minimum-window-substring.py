# Took roughly an hour

from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right = 0, 0

        scoreBoard = defaultdict(int)
        minStuff = {
            'l': float('inf'),
            'subStr': ""
        }
        for c in t:
            scoreBoard[c] += 1
        
        validFlag = False

        # Move right ptr (sub from scoreboard)
        while right < len(s):
            curRightChar = s[right]
            right += 1  # need to think about this ordering
            
            # lower the score (since it exists in substr)
            if curRightChar in scoreBoard:
                scoreBoard[curRightChar] -= 1
    
            if self.checkIfDone(scoreBoard) == True:
                self.updateRet(s, left, right, minStuff)
                validFlag = True

            # If ValidFlag is True, move left
            while validFlag == True:
                curLeftChar = s[left]
                left += 1

                # increase the score (since it exists no longer counted in the substr)
                if curLeftChar in scoreBoard:
                    scoreBoard[curLeftChar] += 1             
                    
                if self.checkIfDone(scoreBoard) == True:
                    self.updateRet(s, left, right, minStuff)
                elif self.checkIfDone(scoreBoard) == False:
                    validFlag = False

        print(minStuff)
        return minStuff['subStr']
    
    def checkIfDone(self, dd):
        for value in dd.values():
            if value > 0:
                return False
        return True
    
    def updateRet(self, s, left, right, minStuff):
        subStr = s[left:right]
        if len(subStr) < minStuff['l']:
            minStuff['l'] = len(subStr)
            minStuff['subStr'] = subStr


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "a"))
    print(s.minWindow("a", "aa"))