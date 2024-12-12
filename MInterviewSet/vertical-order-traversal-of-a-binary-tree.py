# Notes: Use row, column in DFS to keep track of posiotion
# Use annoying postprocessing the sort and write and sort and write
# TC: O(n) (DFS) 
# + O ( nlogn ) O(nlogn) (sorting columns) 
# + O ( nlogn ) O(nlogn) (sorting within columns and groups) 
# = O(nlogn )

# SC O(n) (dict) and O(h) for call stack from DFS

from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dd = defaultdict(list)

        def dfs(root, col, height, dd):
            if root == None:
                return

            dd[col].append( (height,root.val)) #maybe should be a bisect for sorted insert?

            dfs(root.left, col - 1, height +1 ,dd)
            dfs(root.right, col + 1, height +1 ,dd)

            return

        dfs(root, 0, 0, dd)  #O(n) operation

        # post processing
        ret = []
        sortedKeys = sorted(dd.keys()) #k logk operation

        for k in sortedKeys:
            col = sorted(dd[k], key=lambda x: x[0])
            
            # Group values by the first element
            hmOfCol = defaultdict(list)
            for first, second in col:
                hmOfCol[first].append(second)

            # Sort and flatten the groups
            colRet = []
            for key in sorted(hmOfCol):
                colRet.extend(sorted(hmOfCol[key]))

            ret.append(colRet)
        
        print(ret)
        return ret