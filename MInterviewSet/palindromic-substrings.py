# Note: Iterate through the list with and in-> out technique, dont forget to handle double letter (abba)
# TC: O(n^2) because checking for palindrome is O(n) time 
# SC: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ret = 0
        for i in range(len(s)): #O(n)
            ret += self.palindromeCount(s, i,i)

            if i+1 < len(s):
                ret += self.palindromeCount(s, i, i+1)

        print(ret)
        return ret
    
    def palindromeCount(self, s, l, r): #O(n)
        count = 0

        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            count +=1
            l -=1
            r +=1
        return count

sol = Solution()
sol.countSubstrings("abc")
sol.countSubstrings("aaa")
