'''
Time: O(n)
Space: O(c)
Explanation: Sliding windows, but the cool kids on LC are doing it wiht a single loop and default dict
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0 # inclusive
        tail = 0 # exclusive
        maxSubstringLen = 0

        while tail < len(s): 
            # Grow
            tail += 1
            subString = s[head:tail]
            print(subString)
            if (self.noDuplicateLetter(subString)):
                maxSubstringLen = max(maxSubstringLen, len(subString))
            else: # If there is a duplicate letter
                # Shrink
                # Reusing subString here seems like an awful idea
                while (not self.noDuplicateLetter(subString) and head < tail):
                    head += 1
                    subString = s[head:tail]
        return maxSubstringLen

    # Bit of stackoverflow genius
    def noDuplicateLetter(self, s: str) -> int: 
        return len(set(s)) == len(s)


sol = Solution()
s = "abcabcbb"
r1 = sol.lengthOfLongestSubstring(s)
print(r1)

s2 = ""
r2 = sol.lengthOfLongestSubstring(s2)
print(r2) ## should be 0


s3 = "aab"
r3 = sol.lengthOfLongestSubstring(s3)
print(r3)

'''
"abcabcbb"
""
"aab"
"abb"
"aba"
"bb"
"b"
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
'''