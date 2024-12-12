# Note: For Valid Palindrome 2. the trick is try skipping the L or R incase of diversence
# For Valid Palindrome 3, so that recursively
# TC: O(N*N)= O(N^2) - if there is a diverance, we do DFS which is O(N) operation and we might diverge N times
# SC: O(N^2) We need to store all possible combinations of (l,r,k) 
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        isNotAPalindromWithThesePointers = {}
        def dfs(s, k, l, r):
            if (l, r, k) in isNotAPalindromWithThesePointers:
                return False

            if k == -1: # Fail condition removed too many
                return False
            while l < r:

                if s[l] == s[r]:
                    l+=1
                    r-=1
                else: #if they dont equal
                    lSide = dfs(s, k-1, l+1, r) # Skip L letter
                    if lSide:
                        return True
                    rSide = dfs(s, k-1, l, r-1) # Skip R letter
                    if rSide:
                        return True
                    
                    isNotAPalindromWithThesePointers[(l, r, k)] = True
                    return False
            return True
        
        l = 0
        r = len(s)-1
        ret = dfs(s, k, l, r)
        print(ret)
        return ret
    
sol = Solution()
sol.isValidPalindrome("abcdeca", 2)
sol.isValidPalindrome("abbababa", 1)
sol.isValidPalindrome("abc", 1)