from collections import defaultdict
# Time Comp
# O(n) outerloop
# in inner loop each element is only processed once
# O(n)

# Space Comp
# O(m) wherem  is the total number of unique characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h, t = 0, 0 

        dupC = defaultdict(int)
        longestVal = 0
        while h < len(s):
            
            curChar = s[h]
            dupC[curChar] +=1

            while dupC[curChar] > 1:
                tailChar = s[t]
                dupC[tailChar] -=1
                t +=1
            h+=1
            longestVal = max(longestVal, h-t)
        print(longestVal)
        return longestVal

sol = Solution()
sol.lengthOfLongestSubstring("zxyzxyz") # 3
sol.lengthOfLongestSubstring("xxxx") # 1
