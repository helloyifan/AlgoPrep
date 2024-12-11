class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Sanitze the input
        s = s.lower()
        # s = s.replace(':', '')
        # s = s.replace('.', '')
        # s = s.replace(',', '')
        # s = s.replace(' ', '')
        s = ''.join(filter(str.isalnum, s)) #str.isalpha
 
        print(s)
        # Checks
        f, b = 0, len(s)-1
        while f <= b:
            if s[f] != s[b]:
                return False
            f += 1
            b -=1
        return True

sol = Solution()
print(sol.isPalindrome("0P"))