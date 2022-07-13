
# Id argue it's not a dp problem but owell
# Time: O(n * something)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        oddRet = self.helper(s, 0) # 'bab' case
        evenRet = self.helper(s, 1) # 'cbbd' case

        if (len(oddRet) > len(evenRet)):
            return oddRet
        return evenRet


    def helper(self, s: str, tailOffset: int):
        longestSub = ""

        for i, val in enumerate(s):
            head = i
            tail = i + tailOffset # Basically for middle of substring being single or double letter
            while(head >= 0 and tail < len(s)):
                if (s[head] == s[tail]):
                    currentLongestSub = s[head:tail+1]
                    if (len(longestSub) < len(currentLongestSub)):
                        longestSub = currentLongestSub
                    head -= 1
                    tail += 1
                else:
                    break

        return longestSub

sol = Solution()
s = "babad"
r = sol.longestPalindrome(s)
print(r)

s2 = 'cbbd'
r2 = sol.longestPalindrome(s2)
print(r2)

s3 = 'racecarqwertyhgfdszxdcfghj'
r3 = sol.longestPalindrome(s3)
print(r3)

s4 = 'abaxyzzyxf'
r4 = sol.longestPalindrome(s4)
print(r4)

s5 = "it's highnoon"
r5 = sol.longestPalindrome(s5)
print(r5)

s6 = "j"
r6 = sol.longestPalindrome(s6)
print(r6)


'''
"babad"
"cbbd"
"racecarqwertyhgfdszxdcfghj"
"abaxyzzyxf"
"itshighnoon"
"j"
'''