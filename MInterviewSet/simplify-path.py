# I didnt write very elegantly
# Notes: Step 1. Clean u '/' with remove, 
# Step2 Pop stack back to front and build ret
# Step3. when you see '..' handle differently, note that /bro/ski/../..
# means you have to go up twice same with /bro/ski/.././..
# TC: O(n) for each new dir in string we process it in loop lineraly
# SC: O(n) stack grows with the loop
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')

        # Not the prettiest *but used to remove all ''
        while '' in s:
            s.remove('')

        retString = ''
        validPopsStillNeeded = 0
        while len(s) > 0:
            
            # Responsible for cleaning up the '..'
            while len(s) > 0 and validPopsStillNeeded > 0:
                curDir = s.pop()
                if curDir == '.':
                    continue
                elif curDir == '..':
                    validPopsStillNeeded += 1
                else:
                    validPopsStillNeeded -= 1
            
            if len(s) > 0:
                curDir = s.pop()
                if curDir == '.':
                    continue
                elif curDir == '..':
                    validPopsStillNeeded += 1
                else:
                    retString =  '/' + curDir + retString

        if retString == '':
            retString += '/'
        print(retString)
        return retString



sol = Solution()
sol.simplifyPath("/home/") # "/home"
sol.simplifyPath("/home//foo/") #" "/home/foo""
sol.simplifyPath("/home/user/Documents/../Pictures") #"/home/user/Pictures"
sol.simplifyPath("/../") #/
sol.simplifyPath("/.../a/../b/c/../d/./") #/
sol.simplifyPath("/a/./b/../../c/")
sol.simplifyPath('/a/../../b/../c//.//')