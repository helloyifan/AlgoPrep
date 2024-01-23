## Valid attempt but this solution takes too long for a test case 

from collections import defaultdict
from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        h, t = 0 , 0 
        maxRet = 0
        while h < len(s):
            h += 1 #not sure if this is dangerous
            subStr = s[t:h]
            highestLetterCount = self.mostFreqLetterCount(subStr)

            gapsInSubStr = len(subStr) - highestLetterCount
            if gapsInSubStr <= k:
                maxRet = max(maxRet, len(subStr)) # because if the gapsInSubStr can be filled, then its a valid answer
            elif gapsInSubStr > k:
                while gapsInSubStr > k:
                    t += 1
                    subStr = s[t:h]
                    highestLetterCount = self.mostFreqLetterCount(subStr)
                    gapsInSubStr = len(subStr) - highestLetterCount

        return maxRet   

    # This stupid funciton takkes like O(n) so in total its O(n^2)
    # def mostFreqLetterCount(self, s):
    #     dd = defaultdict(int)
    #     for c in s:
    #         dd[c] += 1
    #     maxVal = 0 
    #     for key in dd:
    #         if dd[key] > maxVal:
    #             maxVal = dd[key]
    #     return maxVal

    def mostFreqLetterCount(self, s):
        counts = Counter(s)
        return max(counts.values(), default=0)


if __name__ == '__main__':
    s = Solution()
    # print(s.characterReplacement('ABAB', 2))
    print(s.characterReplacement('AABABBA', 1))
    print(s.characterReplacement('CBAAAABBBBBA', 1))