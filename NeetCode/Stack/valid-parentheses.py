# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        refHelper = {'(': ')', '{': '}', '[':']'}

        stack = []

        for e in s:
            if (e == '(' or e == '[' or e == '{'):
                stack.append(refHelper[e])
            elif (e == ')' or e == ']' or e == '}'): # not needed assumingin put is always valid
                if (len(stack) ==0):
                    return False
                if (e != stack[-1]): # this is equivalent of peek
                    return False
                elif (e == stack[-1]): # should be implicit
                    stack.pop()
        
        return (len(stack) == 0)



sol = Solution()
s = "()[]{}"
r1= sol.isValid(s)
print(r1)

s2 = "("
r2= sol.isValid(s2)
print(r2)

s3 = ")("
r3 = sol.isValid(s3)
print(r3)

s4 = "([)]"
r4 = sol.isValid(s4)
print(r4)
