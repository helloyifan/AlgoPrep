# Imo could be sliding window 
    # Not sure what the conditon would be for moving pointers up
# or dp

# 25min spent: this is worse then the brute force solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}

        maxPalindrome = ""
        maxLen = 0

        for i, c in enumerate(s):
            dp[i] = True
            entryToRemove = []
            for key in dp:
                currentSubString = s[key : i+1]
                if self.isPalindrome(currentSubString):
                    if len(currentSubString) > maxLen:
                        maxLen =len(currentSubString)
                        maxPalindrome = currentSubString
                # else:
                #     entryToRemove.append(key)

            # for e in entryToRemove:
            #     del dp[e]

        return maxPalindrome
    
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
        return True

sol = Solution()
print(sol.longestPalindrome("babad")) #bab
print(sol.longestPalindrome("abb")) #bb


# print(sol.isPalindrome("apple"))
# print(sol.isPalindrome("pap"))