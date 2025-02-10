# Notes: Standard DFS question (can also try with BFS)
# TC: O(n) in the worst case we could visit every single element in array
# SC: O(logn) on average interms of how can levels we go in dfs, worst cast is O(n) in levels deep for DFS on call stack


from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        finPath = []
        def dfs(cur, visited, path):
            if cur < 0 or cur >= len(arr):
                return False

            if arr[cur] == 0:
                path.append(cur)
                finPath.append(path[:])
                path.pop() # need to keep track of backtracking
                return True
            
            if cur in visited:
                return False
            
            visited.add(cur)
            path.append(cur)

            foundTrue = False
            
            l = dfs(cur - arr[cur], visited, path)
            r = dfs(cur + arr[cur], visited, path)
            if l or r:
                foundTrue = True

            visited.remove(cur) # backtracking is fun
            path.pop()

            return foundTrue
        
        ret = dfs(start, set(), [])
        
        print(ret)
        if ret == True:
            print(finPath)
        
        return ret

sol = Solution()
sol.canReach([4,2,3,0,3,1,2], 5) # True 
sol.canReach( [4,2,3,0,3,1,2], 0) # Ture
sol.canReach( [3,0,2,1,2], 2) # Ture


#[3,0,2,1,2], start = 2