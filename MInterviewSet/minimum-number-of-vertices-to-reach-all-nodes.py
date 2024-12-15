from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        # Figuring n degress
        inDegree = [0 for _ in range(n)]
        
        for e in edges:
            inDegree[e[1]] += 1
        
        ret = []
        for i, e in enumerate(inDegree):
            if e == 0:
                ret.append(i) # index represent node identifier

        print(ret)        
        return ret
    
sol = Solution()
sol.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]])
