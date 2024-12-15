# TC: O(n) Sliding window we process each character at most twice
# SC: O(n) if its all repeating character
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        l, r = 0, 0
        dp = defaultdict(int)
        maxFinalResult = 0
        
        # Normally move head
        while r < len(s):
            dp[s[r]] += 1
            
            # Conditionally move tail
            while dp[s[r]] > 1:
            # condition where we move up L
                dp[s[l]] -= 1  
                l+=1
                
            maxFinalResult = max(maxFinalResult, r-l+1)
            r +=1
            
        print(maxFinalResult)
        return maxFinalResult

longest_substring("bbbbb")