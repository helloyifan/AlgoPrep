# Note: watch the time complexity its not O(n) its not nodes we are working with
# TC: O(2^n) each element we have two choices to include or not
# SC: O(2^n) for [1,2,3] we will have 2^3 results 
# O(height) which is O(logn) for a balanced tree, and its O(n) for a skewed tree so its O(n)
# SC total is O(2^n * n) so its O(2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, i, listOfNums):
            if i == len(nums):
                return [listOfNums[:]]
            
            curRet = [] #list of list of nums

            listOfNums.append(nums[i]) # include curNum
            includeCurNum = dfs(nums, i+1, listOfNums)
            curRet.extend(includeCurNum)

            listOfNums.pop() # don't include it

            notIncludeCurLetter = dfs(nums, i+1, listOfNums)
            curRet.extend(notIncludeCurLetter)

            return curRet
        
        ret = dfs(nums, 0, [])
        return ret
