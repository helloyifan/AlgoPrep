# Notes: This is kinda weirdly worded question
# Basically the thing to note is that,
# you want to generate the multiple subsequence of source
# that when appended together, is target

# TC: O(m*n)
# SC: O(n)

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # What if the target has something source doesnt have?
        # should we fail fast?
        sourceSet = set() # O(n)
        for i in source: # O(n)
            sourceSet.add(i)

        for i in target: # O(n)
            if i not in sourceSet:
                #print(-1)
                return -1

        # ret 
        subsequenceCounter = 0
        
        # if we ever get to the end of source Ptr we reset
        targetIndex = 0 
        while targetIndex < len(target): # O(m)
            #print(targetIndex)
            subsequenceCounter += 1
            firstMatchFound = False
            for sourceIndex, sourceChar in enumerate(source):  # O(n)
                if targetIndex == len(target):
                    print('hhuh')
                    break
                
                targetChar = target[targetIndex]
                
                if targetChar == sourceChar:
                    targetIndex += 1
                    if firstMatchFound == True:
                        # Theres a match and, its not the first, great do nothing
                        continue
                    else:  # First time with current subsequence that we found a mtch
                        firstMatchFound = True
                        continue

sol = Solution()
sol.shortestWay("abc", "abcbc") # return 2
sol.shortestWay("abc", "acdbc") # this returns -1
sol.shortestWay("xyz", "xzyxz") # this returns 3