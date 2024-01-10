class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        unfiltered_rets = self.helper(candidates, target)
        final_ret = self.helper_filter(unfiltered_rets)
        return final_ret
    
    def helper_filter(self, unfiltered_rets):
        set_ret = []

        for r in unfiltered_rets:
            s = sorted(r)
            set_ret.append(s) if not s in set_ret else None
        
        return set_ret

    def helper(self, candidates, t):
        if t == 0:
            return [[]]
        
        cur_rets = []
        for c in candidates:
            sub_val = t - c

            if sub_val >= 0:
                lower_level_rets = self.helper(candidates, sub_val)
                if lower_level_rets and len(lower_level_rets) >0:
                    for ret in lower_level_rets:
                        ret.append(c) #If we want to optimize we would add this to a counter {2:2, 3:2}
                    cur_rets.extend(lower_level_rets)
        return cur_rets

    
if __name__=="__main__":
    sol = Solution()
    r1 = sol.combinationSum([2,3,6,7], 7)
    print(r1)
    
    r2 = sol.combinationSum([2,3,4], 40)
    print(r2)
    