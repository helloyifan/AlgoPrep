# The category is BinSearch,
# However logically we arn't exactly performing binary search, this is binary tree based solution

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.helper(nums, target, 0, len(nums)-1)
    
    def helper(self, nums, target, s, e):
        if s == e:
            return s if nums[s] == target else -1
        elif s > e:
            return -1
        
        midIndex = (s+e)//2
        midValue = nums[midIndex]

        if midValue == target:
            return midIndex
        
        l = self.helper(nums, target, s, midIndex)
        r = self.helper(nums, target, midIndex + 1, e )
        return max(l,r)

if __name__ == '__main__':
    sol = Solution()
    print(sol.search( [4,5,6,7,0,1,2], 0))

    print(sol.search( [4,5,6,7,0,1,2], 8))

    print(sol.search( [1], 0))

    print(sol.search( [1], 1))