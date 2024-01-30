# took me 30 mins but not sure if its true dp because i guess im using the max

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        maxPalindrome = ""
        for i, e in enumerate(s):
            l, r = i , i 
            
            tempPalindrome = self.helper(s, l, r)
            if len(tempPalindrome) > maxLen:
                maxLen = len(tempPalindrome)
                maxPalindrome = tempPalindrome

            # Run it again if repeating letter case cbbds
            if r < len(s)-1 and e == s[r+1]:
                r += 1
                tempPalindrome = self.helper(s, l, r)
                if len(tempPalindrome) > maxLen:
                    maxLen = len(tempPalindrome)
                    maxPalindrome = tempPalindrome

        return maxPalindrome
    
    def helper(self, s, l ,r):
        while l-1 >= 0 and r+1 < len(s):
            if s[l-1] == s[r+1]:
                l -= 1
                r += 1

            else:
                break
        return s[l: r+1]

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    # Output: "bab"
    # Explanation: "aba" is also a valid answer.

    print(s.longestPalindrome("cbbd"))
    # Output: "bb"

    print(s.longestPalindrome("ccc"))
    