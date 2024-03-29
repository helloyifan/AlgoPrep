# very messy code, dont bother studying it too much its not that celever

class Solution():
    def exist(self, grid, s):
        firstChar = s[0]
        self.grid = grid
        
        self.rowSize = len(grid) 
        self.colSize = len(grid[0])

        for ri, row in enumerate(self.grid):
            for ci, col in enumerate(row):
                if col == firstChar:
                    r = self.helper(s[1:], [{'r': ri, 'c': ci}])
                    if r == True:
                        return True     
        return False

    def helper(self, s, l):
        if len(s) == 0:
            return True
        
        r, c = l[-1]['r'], l[-1]['c']
        nextChar = s[0]

        flag = False

        if r - 1 >= 0 and not {'r': r-1, 'c': c}  in l and self.grid[r - 1][c] == nextChar:
            lCopy = l[:]
            lCopy.append({'r': r-1, 'c': c})
            flag = self.helper(s[1:], lCopy)

        if r + 1 < self.rowSize and not{'r': r+1, 'c': c}  in l and self.grid[r + 1][c] == nextChar:
            lCopy = l[:]
            lCopy.append({'r': r+1, 'c': c})
            flag = flag or self.helper(s[1:], lCopy)
        
        if c - 1 >= 0 and not {'r': r, 'c': c-1 }  in l and self.grid[r][c - 1] == nextChar:
            lCopy = l[:]
            lCopy.append({'r': r, 'c': c-1})
            flag = flag or self.helper(s[1:], lCopy)

        if c + 1 < self.colSize and not {'r': r, 'c': c+1 }  in l and self.grid[r][c + 1] == nextChar:
            lCopy = l[:]
            lCopy.append({'r': r, 'c': c+1})
            flag = flag or self.helper(s[1:], lCopy)

        if flag == False:
            return False
        
        return True
        

if __name__ == "__main__":
    s = Solution()
    t1 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print(s.exist(t1, "ABCCED")) #True
    print(s.exist(t1, "SEE")) # True
    print(s.exist(t1, "ADEE")) # True
    print(s.exist(t1, "ADEZ")) # False
    print(s.exist(t1, "ABCB")) # False
    t2 = [
        ["A", "B"],
    ]
    print(s.exist(t2, "BA")) # True
    t3 = [
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]
    ]
    print(s.exist(t3, "AAB")) # True