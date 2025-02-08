# Note: The trick is to respect that when you kick the ball, it goes all the way to the end
# No need to BFS on a single step, bfs to the end

# TC: O(m*n) (based on the size of the matrix)
# SC: O(m*n) for the q that could have every square in it in the worst case
from typing import List
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        maxR, maxC = len(maze) -1, len(maze[0]) -1
        startTuple = (start[0], start[1])
        q = deque()
        q.append(startTuple)
        
        visited = set()
        while len(q) > 0:
            tempQ = deque()

            while len(q) > 0:
                cur = q.popleft()
                r,c = cur[0], cur[1]
                
                if cur[0] == destination[0] and cur[1] == destination[1]:
                    return True

                if cur in visited:
                    continue
                visited.add(cur)
                
                dirs = [(0,1), (1,0), (-1,0), (0,-1)]
                for d in dirs:
                    newR, newC = r, c

                    while (0 <= newR+d[0] <= maxR) and (0 <= newC+d[1] <= maxC) and maze[newR+d[0]][newC+d[1]] == 0:
                        newR += d[0]
                        newC += d[1]
                    tempQ.append((newR,newC))

            q = tempQ
        #print(visited)
        return False
sol = Solution()
print(sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],  [0,4], [4,4]))
print(sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],  [0,4], [3,2]))