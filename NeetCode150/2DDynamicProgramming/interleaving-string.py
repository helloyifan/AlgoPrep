# 20 min thinking
# 7 min to implement the recursive solution
# dp sol, need to watch video i have no idea
class Solution:
    def recursiveSolution(self, s1: str, s2: str, s3: str) -> bool:
        def helper(ts1, ts2, ts3):
            if len(ts3) == 0:
                if len(ts1) > 0 or len(ts2) > 0:
                    return False
                return True

            leftRet = False
            rightRet = False
            if len(ts1) > 0 and ts1[0] == ts3[0]:
                leftRet = helper(ts1[1:], ts2, ts3[1:])
            
            if len(ts2) > 0 and ts2[0] == ts3[0]:
                rightRet = helper(ts1, ts2[1:], ts3[1:])

            return leftRet or rightRet
        ret = helper(s1, s2, s3)
        print(ret)
        return ret

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.recursiveSolution(s1,s2,s3)
        

if __name__ == "__main__":
    # t1 is true
    t1s1 = "aabcc"
    t1s2 = "dbbca"
    t1s3 = "aadbbcbcac"

    # t2 is false
    t2s1 = "a"
    t2s2 = "b"
    t2s3 = "a"


    sol = Solution()
    sol.recursiveSolution(t1s1, t1s2, t1s3)
    sol.recursiveSolution(t2s1, t2s2, t2s3)
