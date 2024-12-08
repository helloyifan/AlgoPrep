# Note: 2 pass, keep track of invalids, create a new string that avoids invalids
# TC: O(2n) = O(n)
# SC: O(n) for index indexOfInvalidOpen and O(n) for index indexOfInvalidClose and O(n) for result = O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexOfInvalidOpen = []
        indexOfInvalidClose = []
        for i, e in enumerate(s):
            if e == "(":
                indexOfInvalidOpen.append(i)
            elif e == ")":
                if len(indexOfInvalidOpen) > 0: # No longer and invalid open
                    indexOfInvalidOpen.pop()
                else:
                    indexOfInvalidClose.append(i)
                
        newStr = ""
        openC = 0
        closeC = 0
        for i, e in enumerate(s):
            if openC < len(indexOfInvalidOpen) and i == indexOfInvalidOpen[openC]:
                openC += 1
            elif closeC < len(indexOfInvalidClose) and i == indexOfInvalidClose[closeC]:
                closeC += 1
            else:
                newStr += e

        print(newStr)
        return newStr
sol = Solution()

sol.minRemoveToMakeValid("lee(t(c)o)de)")
sol.minRemoveToMakeValid("a)b(c)d")
sol.minRemoveToMakeValid("))((")
sol.minRemoveToMakeValid(")")
sol.minRemoveToMakeValid("")