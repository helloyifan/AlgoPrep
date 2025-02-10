# Notes: Standard DFS question (can also try with BFS)
# TC: O(n) in the worst case we could visit every single element in array
# SC: O(logn) on average interms of how can levels we go in dfs, worst cast is O(n) in levels deep for DFS on call stack


from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(cur, visited):
            if cur < 0 or cur >= len(arr):
                return False

            if arr[cur] == 0:
                return True
            
            if cur in visited:
                return False
            
            visited.add(cur)

            foundTrue = False
            
            foundTrue = dfs(cur - arr[cur], visited)
            if foundTrue == False:
                foundTrue = dfs(cur+arr[cur], visited)

            visited.remove(cur) # backtracking is fun

            return foundTrue
        
        ret = dfs(start, set())
        
        print(ret)
        return ret

sol = Solution()
sol.canReach([4,2,3,0,3,1,2], 5) # True 
sol.canReach( [4,2,3,0,3,1,2], 0) # Ture
sol.canReach( [3,0,2,1,2], 2) # Ture


#[3,0,2,1,2], start = 2