# Note: The intuitve solution is to use two pointers
# But there are are countless ways on LC, that might be more efficient

# TC: O(T) - sicnce we are checking everything in t and t is bigger then s
# SC: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Stupid edge case
        if len(s) == 0:
            return True
        
        p1=0

        for p2, e2 in enumerate(t):
            e1 = s[p1]
            if e1 == e2:
                p1 += 1
        
            if p1 == len(s):
                return True
        return False