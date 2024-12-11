# TC: O(n) minLengthOfWord, O(nxm) n = number of words, m = minLengthOfWord
# SC: O(1)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLengthOfWord = float('inf')
        for s in strs:
            minLengthOfWord = min(minLengthOfWord, len(s))
        
        lastIndex = 0
        for n in range(minLengthOfWord):
            curLetter = None
            for s in strs:
                if curLetter == None:
                    curLetter = s[n]
                else:
                    if curLetter != s[n]:
                        return strs[0][:lastIndex]
            lastIndex += 1

        return strs[0][:lastIndex]


# print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["aaaa","aa","a"]))
               