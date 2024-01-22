from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dp = defaultdict(int)
        for s_char in s:
            dp[s_char] += 1

        for t_char in t:
            dp[t_char] -= 1

        for key in dp:
            if dp[key] != 0:
                return False
        return True
