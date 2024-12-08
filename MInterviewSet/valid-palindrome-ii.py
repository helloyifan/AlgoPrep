# Notes: When you encounter a mismatch, you have to either remove f or b, but you need to explore both to see whats possible
# A more advanced palindrom check is s[:] == s[::-1]
# TC: O(3n) because we are potentially making 3 passes, total is O(n)
# SC:We are making copies of the string with character removed so also O(n) 

class Solution:
    def validPalindrome(self, s: str) -> bool:
        pass1, f, b = self.validPalindromeHelper(s)
        if pass1 == True:
            return True
        else:
            # removedString1 = s[:f] + s[f+1:]
            # Instead of rechecking the whole string, we can pick up where we left off
            # Remember back is exclusive
            removedString1 = s[f+1:b+1] 
            
            pass2, f2, b2 = self.validPalindromeHelper(removedString1)
            if pass2 == True:
                return True 

            # removedString2 = s[:b] + s[b+1:]
            removedString2 = s[f:b] # since front is inclusive we leave it as f
            pass3, f3, b3 = self.validPalindromeHelper(removedString2)
            if pass3 == True:
                return True

            return False
    def validPalindromeHelper(self, s: str) -> bool:
        f, b = 0, len(s)-1
        while f < b:
            if s[f] == s[b]:
                f +=1
                b -=1
            else:
                return False, f, b
        return True, None, None 

sol = Solution()
print(sol.validPalindrome("aba")) # True
print(sol.validPalindrome("abba"))# True
print(sol.validPalindrome("abbca"))# True
print(sol.validPalindrome("abc")) # False
print(sol.validPalindrome("aaaabc"))# False
print(sol.validPalindrome("abbc")) # False
print(sol.validPalindrome("a")) # True

print(sol.validPalindrome("eceec")) # True
print(sol.validPalindrome("cbbcc")) # True
