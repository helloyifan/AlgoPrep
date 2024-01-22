from collections import defaultdict
import copy

class Solution():
    def combinationSum(self, nums, t):
        allDDs = self.helper(nums, t, defaultdict(int))
        ret = []
        for dd in allDDs:
            tempRet = self.convertDDToList(dd)
            if not tempRet in ret:
                ret.append(tempRet)
        return ret
    
    def helper(self, nums, t, dd):
        if t == 0:
            return [dd]
        elif t < 0:
            return None

        collectiveRet = []
        for num in nums:
            newDD = copy.copy(dd)
            newDD[num] +=1
            ret = self.helper(nums, t - num, newDD)
            # Handle deduping here
            if ret != None:
                collectiveRet.extend(ret)
        return collectiveRet
    
    def convertDDToList(self, dd):
        ret = []
        for key in dd:
            val = dd[key]
            for i in range(val):
                ret.append(key)
        ret = sorted(ret)
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7)) #[2,2,3] [7]
    print(s.combinationSum([2, 3, 5], 8)) 
    print(s.combinationSum([2], 1)) 