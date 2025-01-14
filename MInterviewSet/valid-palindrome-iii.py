# Note: For Valid Palindrome 2. the trick is try skipping the L or R incase of diversence
# For Valid Palindrome 3, so that recursively
# TC: O(N^2 *k)
# There are N different possiblity for L and N different possibilities for R so together is O(N^2)
# We will have k diverance so its O(N^2 *k)
# SC: O(N^2 *k) We need to store all possible combinations of (l,r,k) 
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        isNotAValidPalindrome = {}

        def dfs(s, l, r, misMatchCounter):
            if (l,r,misMatchCounter) in isNotAValidPalindrome:
                return False
            if misMatchCounter > k:
                return False
            
            while l < r:
                if s[l] != s[r]:
                    lRet = dfs(s, l+1, r, misMatchCounter + 1)
                    if lRet == True:
                        return True
                    rRet = dfs(s, l, r-1, misMatchCounter + 1)
                    if rRet == True:
                        return True
                    isNotAValidPalindrome[(l,r,misMatchCounter)] = True
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        ret = dfs(s, 0, len(s)-1, 0)
        print(ret)
        return ret
    
sol = Solution()
sol.isValidPalindrome("abcdeca", 2)
sol.isValidPalindrome("abbababa", 1)
sol.isValidPalindrome("abc", 1)