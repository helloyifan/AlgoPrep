## Valid attempt but this solution takes too long for a test case 
# >>> a = {'a': 1, 'b':2}
# >>> a.values()
# dict_values([1, 2])
# >>> a.keys()
# dict_keys(['a', 'b'])
# >>> max(a)
# 'b'
# >>> max(a.values())
# 2
from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        h, t = 0 , 0 
        maxRet = 0
        dd = defaultdict(int) # This is frequency tracker
        while h < len(s):
            h += 1 #not sure if this is dangerous
            dd[s[h-1]] += 1 # h-1 because s[t:h] does not include
            subStr = s[t:h]
            highestLetterCount = max(dd.values())
            gapsInSubStr = len(subStr) - highestLetterCount
            if gapsInSubStr <= k:
                maxRet = max(maxRet, len(subStr)) # because if the gapsInSubStr can be filled, then its a valid answer
            elif gapsInSubStr > k:
                while gapsInSubStr > k:
                    t += 1
                    dd[s[t-1]] -= 1 #count down if the char moved out of the window
                    subStr = s[t:h]
                    highestLetterCount = max(dd.values())
                    gapsInSubStr = len(subStr) - highestLetterCount

        return maxRet   


if __name__ == '__main__':
    s = Solution()
    print(s.characterReplacement('ABAB', 2))
    print(s.characterReplacement('AABABBA', 1))
    print(s.characterReplacement('CBAAAABBBBBA', 1))
    print(s.characterReplacement('ABAA', 0))