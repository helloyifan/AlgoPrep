class Solution:
    def numIslands(self, grid):
        self.grid = grid
        self.rowSize = len(grid) - 1
        self.colSize = len(grid[0]) - 1

        ret = 0
        for ri, row in enumerate(self.grid):
            for ci, col in enumerate(row):
                if self.grid[ri][ci] == '1':
                    self.flipAllConnectedToZero({'r': ri, 'c': ci})
                    ret += 1
        return ret
    
    def flipAllConnectedToZero(self, loc):
        r, c = loc['r'], loc['c']
        self.grid[r][c] = '0'

        dirs = [{'r': r-1, 'c': c}, {'r': r+1, 'c': c}, {'r': r, 'c': c-1}, {'r': r, 'c': c+1}]

        for dir in dirs:
            if (0 <= dir['r'] <= self.rowSize and 
                0 <= dir['c'] <= self.colSize and 
                self.grid[dir['r']][dir['c']] == '1'): 
                    self.flipAllConnectedToZero(dir)
        return

if __name__ == '__main__':
    s = Solution()
    g1 = [
        ['1','1','1','1','0'],
        ['1','0','1','1','0'],
        ['1','0','0','0','0'],
        ['0','0','0','0','0']
    ]
    print(s.numIslands(g1))
    g2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(s.numIslands(g2))
    g3 = [
        ["1","0","1","0","1"],
    ]
    print(s.numIslands(g3))
    g4 = [
        ["1","1","0","1","0"],
    ]
    print(s.numIslands(g4))
    g5 = [
        ["1"],
    ]
    print(s.numIslands(g5))
