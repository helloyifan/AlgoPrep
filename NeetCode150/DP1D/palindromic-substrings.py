class Solution:
    def countSubstrings(self, s: str) -> int:
        c = {'counter': 0 } 

        for i, val in enumerate(s):
            self.palindromVerifier(s, i, i, c)

            if (i > 0):
                self.palindromVerifier(s, i-1, i, c)
                
        return c['counter']
    
    def palindromVerifier(self, s, start1, start2, c):
        p1 = start1
        p2 = start2

        while(True):
            if (p1 < 0 and p2 >= len(s)): # base case basically
                return True # or break
            if (p1 < 0 and p2 < len(s)):
                return False 
            if (p1 >= 0 and p2 >= len(s)):
                return False
            if (s[p1] != s[p2]):
                return False
            
            p1 -= 1
            p2 += 1
            c['counter'] += 1

        return True


'''
Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''


s = Solution()
s1 = 'abc'
r1 = s.countSubstrings(s1)
print(r1)

s2 = 'aaa'
r2 = s.countSubstrings(s2)
print(r2)


s3 = 'a'
r3 = s.countSubstrings(s3)
print(r3)

'''
"abc"
"a"
"racecar"
"aaaaaagaaaaa"
"aaaaaaggaaaaa"
'''