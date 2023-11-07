from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dp = {}
        for s in strs:
            ## Build key
            sortedKey = sorted(s)
            keyString = self.createStringFromList(sortedKey)

            if (keyString in dp):
                dp[keyString].append(s)
            else:
                dp[keyString] = [s]
        
        ret = []
        for key in dp:
            ret.append(dp[key])
        
        return ret

    def createStringFromList(self, lst):
        ret = ''
        for i in lst:
            ret = ret + i
        return ret

s = Solution()
t1 = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
r1 = s.groupAnagrams(t1)
print(r1)

t2 = ['']
r2 = s.groupAnagrams(t2)
print(r2)

t3 = ['a']
r3 = s.groupAnagrams(t3)
print(r3)