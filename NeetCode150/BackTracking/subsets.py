# Took 16 mins , but learned how to use copy, was struggling with deepcopy debug


from typing import List
import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(nums):
            if len(nums) == 0:
                return [[]]

            prev = helper(nums[1:])
            #prev2 = [item[:] for item in prev]# This works I cant do just prev[:] because the inner list is shallow copied
            #copy = [item[:] for item in prev] 

            # Better practice is to use copy
            prev2 = copy.deepcopy(prev)
            prev3 = copy.deepcopy(prev)

            for i in prev3:
                i.append(nums[0])


            # This also works
            # ret = prev3 + prev2          
            # return ret
            # But doing this instead
            prev3.extend(prev2)
            return prev3
        
        finret = helper(nums)
        print(finret)
        return finret
    
if __name__ == '__main__':
    sol = Solution()

    sol.subsets([1,2,3]) #[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    sol.subsets([7]) # [[],[7]]