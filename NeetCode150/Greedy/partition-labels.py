# Solved in 30 minute ish
# Run time complexity
#  O(n): its O(n) to preprocess and O(n) to process
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occuranceDict = {}

        for i, e in enumerate(s):
            if not e in occuranceDict:
                occuranceDict[e] =[i,i] #min and max are both current occurance
            else:
                old = occuranceDict[e]
                newMin = min(old[0], i)
                newMax = max(old[1], i)
                occuranceDict[e] = [newMin, newMax]
        print(occuranceDict)
        l = []
        # convert dict to a list
        for key in occuranceDict:
            l.append(occuranceDict[key])

        # sort list (may be redundant)
        #l.sort(key=lambda x: x[0]) # sort by first element of list
        
        ret =[]
        curStart = None
        curEnd = None
        for i, e in enumerate(l):
            if curStart == None:
                curStart = e[0]
            
            if curEnd == None:
                curEnd = e[1]
            else:
                # If prev letter in the range of e
                if curEnd > e[0] and curEnd < e[1]:
                    curEnd = e[1]
                elif curEnd <= e[0]:
                    ret.append(curEnd - curStart + 1)
                    curStart = e[0]
                    curEnd = e[1]
        # Left over (add it in too)
        ret.append(curEnd - curStart + 1)

        print(ret)
        return ret

sol = Solution()
sol.partitionLabels("xyxxyzbzbbisl") # [5, 5, 1, 1, 1]
sol.partitionLabels("abcabc") # [6]
sol.partitionLabels("ababcbacadefegdehijhklij") # [9,7,8]
