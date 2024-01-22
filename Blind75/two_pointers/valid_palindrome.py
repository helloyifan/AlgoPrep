class Solution():
    def validPalindrome(self, strVal):
        strVal = self.remove_non_alpha(strVal.lower())
        h, t = 0, len(strVal) - 1 
        while h < t:
            if strVal[h] != strVal[t]:
                return False
            h += 1
            t -= 1

        return True
    
    def remove_non_alpha(self, strVal):
        ret = ''
        for c in strVal:
            if c.isalpha():
                ret += c
        return ret
if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome("A man, a plan, a canal: Panama"))
    print(s.validPalindrome('race a car')) # not a palindrome
    print(s.validPalindrome(' '))