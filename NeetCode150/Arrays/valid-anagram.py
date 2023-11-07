from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dp = defaultdict(int)

        for i, val in enumerate(s):
            dp[val] += 1
        
        for i, val in enumerate(t):
            dp[val] -= 1

        for i, val in enumerate(dp):
            if(dp[val] != 0):
                return False
        return True

s = Solution()

s1 = "anagram"
t1 = "nagaram"
r1 = s.isAnagram(s1, t1)
print(r1)

s2 = "rat"
t2 = "car"
r2 = s.isAnagram(s2, t2)
print(r2)


s3 = "rat"
t3 = ""
r3 = s.isAnagram(s3, t3)
print(r3)


s4 = "rat"
t4 = "ratt"
r4 = s.isAnagram(s4, t4)
print(r4)