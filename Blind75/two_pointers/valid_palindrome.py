class Solution():
    def isPalindrome(self, strVal):
        strVal = self.remove_non_alpha_numeric(strVal.lower())
        h, t = 0, len(strVal) - 1 
        while h < t:
            if strVal[h] != strVal[t]:
                return False
            h += 1
            t -= 1

        return True
    
    def remove_non_alpha_numeric(self, strVal):
        ret = ''
        for c in strVal:
            # if c.isalpha(): to check if alphabetic
            if c.isalnum():
                ret += c
        return ret
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome('race a car')) # not a palindrome
    print(s.isPalindrome(' '))
    print(s.isPalindrome('0P'))