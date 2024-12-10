# Imo could be sliding window 
    # Not sure what the conditon would be for moving pointers up
# or dp

# 25min spent: this is worse then the brute force solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestPalindromeWithOffSetTracker(s, offset):
            maxPalindrome = ""
            maxLen = 0
        
            for i in range(len(s)):
                f, b= i, i + offset
                while 0 <= f and b < len(s) and f <= b and s[f] == s[b]:                    
                    # Max len
                    curMaxLen = b-f + 1 # adding one bcuz ind - ind is 0, but the word len is 1
                    if maxLen < curMaxLen:
                        maxLen = curMaxLen
                        maxPalindrome = s[f:b+1] #+1 offset to be inclusive
                    f-=1
                    b+=1
            return maxLen, maxPalindrome
        
        maxOddLen, maxOddWord = longestPalindromeWithOffSetTracker(s, 0)
        maxEvenLen, maxEvenWord = longestPalindromeWithOffSetTracker(s, 1)

        finRet = maxOddWord
        if maxEvenLen > maxOddLen:
            finRet = maxEvenWord
        return finRet

sol = Solution()
print(sol.longestPalindrome("babad")) #bab
print(sol.longestPalindrome("abb")) #bb


print(sol.longestPalindrome("apple"))
print(sol.longestPalindrome("pap"))
print(sol.longestPalindrome("a"))