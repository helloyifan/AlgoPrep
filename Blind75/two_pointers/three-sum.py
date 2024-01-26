# 20 min spent need more debugging
# 15 min debugging later in the night

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        ret = []
        
        for i, num in enumerate(sorted_nums):
            if i == len(sorted_nums) - 2:
                continue
            target = sorted_nums[i] 
            remaining_list = sorted_nums[i+1:] # Front is inclusive

            left = 0
            right = len(remaining_list) -1

            while left < right: #left >= 0 and right < len(remaining_list):
                total = remaining_list[left] + remaining_list[right]
                if total + target == 0:
                    tempRet = [target,  remaining_list[left], remaining_list[right]]
                    if tempRet not in ret:
                        ret.append(tempRet)
                        
                # Target is a negative number
                # With abs its still a bit complicated
                if total < abs(target):
                    left += 1
                elif total >= abs(target):
                    right -= 1

                else:
                    raise("Something bad happened")
        return ret
    

if __name__ == '__main__':
    s = Solution()
    # print(s.threeSum([-1,0,1,2,-1,-4]))
    # print(s.threeSum([0, 1, 1]))
    # print(s.threeSum([0, 0, 0]))
    # print(s.threeSum([0, 0, 0, 0]))
    # print(s.threeSum([1,-1,-1,0]))
    print(s.threeSum([-2,0,1,1,2]))