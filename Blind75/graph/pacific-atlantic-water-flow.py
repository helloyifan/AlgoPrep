# Attempt 1: Pretty straight forwards some debugging time under 1 hour 
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.lastRow = len(heights) - 1
        self.lastCol = len(heights[0]) - 1
        ret = []
        for ri, r in enumerate(heights):
            for ci, c in enumerate(r):
                paRet = self.dfs(heights, ri, ci, [])

                if 'p' in paRet and 'a' in paRet:
                    ret.append([ri, ci])

        return ret
    
    def dfs(self, heights, r, c, traversed):
        if r < 0 or c < 0:
            return 'p'# hit pacific :)!
        elif r > self.lastRow or c > self.lastCol:
            return 'a' # hit atlantic or w.e

        dirs = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
        pFlag, aFlag = False, False

        for dir in dirs:
            # Since water can flow if its the same level, we need to check that we are not going back and fourth
            if dir in traversed:
                # if this dir is the same from the way we came, we just skip this dir
                continue

            curVal = heights[r][c]

            # If its out of bounds, then its 0 height, which makes sense
            if dir[0] < 0 or dir[0] > self.lastRow or dir[1] < 0 or dir[1] > self.lastCol:
                peekDirVal = 0 
            else:
                peekDirVal = heights[dir[0]][dir[1]]

            # if the current cell we are on is taller then the dir cell 
            if curVal >= peekDirVal:
                traversed.append(dir)
                tempRet = self.dfs(heights, dir[0], dir[1], traversed)
                if 'p' in tempRet:
                    pFlag = True
                if 'a' in tempRet:
                    aFlag = True

                if pFlag == True and aFlag == True: # Optimiation, if its already true, we can stop
                    break


        
        # Silly flags 'pa' means touching bouth pacific and atlantic
        ret = ''
        if pFlag:
            ret = ret + 'p'
        if aFlag:
            ret = ret + 'a'
        return ret

if __name__ == '__main__':
    s = Solution()
    t1 = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    print(s.pacificAtlantic(t1)) #[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    t2 = [
        [1,1],
        [1,1]
    ]
    print(s.pacificAtlantic(t2)) #[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
