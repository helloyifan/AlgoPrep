class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        odds = self.helper(s, 0)
        evens = self.helper(s, 1)

        if len(odds) > len(evens):
            return odds
        return evens
        
    
    def helper(self, s, isEven):
        l = len(s)
        maxBruh = float('-inf')
        maxSubStr = ''
        
        for i in range(0, l):
            f, b = i, i + isEven

            while f >= 0 and b < l and s[f] == s[b]:
                if (b-f + 1) > maxBruh:
                    maxBruh = (b-f + 1)
                    maxSubStr= s[f:b+1]

                f = f-1
                b = b+1
        return maxSubStr
    
if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome("babad"))
    # print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
