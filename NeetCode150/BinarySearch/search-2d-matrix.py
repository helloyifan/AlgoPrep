from typing import List
# Took 20 mins
# Bunch of edge cases but yeah just used binary search twice 
class Solution:
    def search(self, list, target, rowMode):
        f, b = 0, len(list) -1 
        while f <= b:
            mid = (f+b)//2
            if list[mid] == target:
                return mid
            elif list[mid] < target:
                f = mid + 1
            else:
                b = mid - 1

        if rowMode: #Edge case where Binary search goes above it
            if list[mid] > target:
                return mid -1

        return mid if rowMode else -1
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def buildFirCol():
            ret = []
            for r in matrix:
                ret.append(r[0])
            return ret
        
        firstCols = buildFirCol()
        rowIndex = self.search(firstCols, target, True)
        print(rowIndex)
        ret = self.search(matrix[rowIndex], target, False)
        print(ret)
        return True if ret != -1 else False

if __name__ == "__main__":
    sol = Solution()
    # sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 1)

    # sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 13)

    # sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 14)
    # sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)

    # sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11)