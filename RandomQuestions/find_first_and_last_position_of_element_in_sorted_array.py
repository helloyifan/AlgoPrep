class Solution(object):
    def searchRange(self, nums, target):
        
        start =self.firstInstanceBinarySearch(nums, target)

        if start == -1 or start > len(nums)-1 or nums[start] != target:
            return [-1, -1]
        
        end = self.firstInstanceBinarySearch(nums, target+1)

        return [start, end -1]
    
    def firstInstanceBinarySearch(self, nums, target):
        if len(nums) == 0:
            return -1

        s = 0
        e = len(nums) -1
        while (s <= e):
            curIndex = (s+e)//2
            curVal = nums[curIndex]
            if (curVal < target): 
                # note, its important that its < and not <=
                # because if curVal is equal to target, we still wanna move the index down
                # this is to find the first occurance
                s = curIndex +1 
            else:
                e = curIndex -1
        return s


if __name__ == "__main__":
    sol = Solution()

    # For learning
    # learn1 = sol.firstInstanceBinarySearch([0,8,8,8,8,8,8,8], 8)
    #print(learn1) # this reutrns index 1

    # ret1 = sol.searchRange([5,7,7,8,8,10], 8)
    # print(ret1)

    # ret2 = sol.searchRange([5,7,7,8,8,10], 6)
    # print(ret2)

    # ret3 = sol.searchRange([], 0)
    # print(ret3)

    ret4 = sol.searchRange([2,2], 3)
    print(ret4)

    ret5= sol.searchRange([-1000,1,2,3,4,5,7,7,8,8,10,11,12,13], 8)
    print(ret5)
