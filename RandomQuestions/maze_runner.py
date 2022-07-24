## MY solution at the maze runner problem
# Basically using DFS where we only track the history for each branch to avoid revisit
# We also build the resulting path on our way back up the call stack

class Solution:
    def solution(self, array):
        ret, retList = self.dfs(array, [], 0, 0)
        if (ret):
            return retList
        
        return 'No Solution'
    
    def dfs(self, array, visited, x, y):
        for i in visited:
            if (i == [x, y]):
                return False, None
        
        visited.append([x,y])

        if (y < 0 or y >= len(array)):
            return False, None

        if (x < 0 or x >= len(array[0])):
            return False, None

        if (array[y][x] == 0): ## Hit way, fast fail
            return False, None
        elif(array[y][x] == 3):  ## Found cheese, base case
            return True, [[y, x]] ## Set true to let us know on our way back

        rightCond, rightLoc = self.dfs(array, visited, x - 1, y)
        if (rightCond): # If the path is a viable path
            rightLoc.insert(0, [y,x]) ## We return back up the stack by appending the cur loc (insert cur loc) at front of list
            return True, rightLoc

        leftCond, leftLoc = self.dfs(array, visited, x + 1, y)
        if (leftCond):
            leftLoc.insert(0, [y,x])
            return True, leftLoc

        upCond, upLoc =  self.dfs(array, visited, x, y - 1)
        if (upCond):
            upLoc.insert(0, [y,x])
            return True, upLoc

        downCond, downLoc = self.dfs(array, visited, x, y + 1)
        if (downCond):
            downLoc.insert(0, [y,x])
            return True, downLoc       
        
        return False, None

sol = Solution()


i1 = [
    [ 1, 1, 0, 0, 0 ],
    [ 0, 1, 0, 0, 0 ],
    [ 0, 1, 1, 1, 0 ],
    [ 0, 1, 0, 0, 0 ],
    [ 0, 1, 1, 3, 0 ]
]
r1 = sol.solution(i1)
print(r1)


