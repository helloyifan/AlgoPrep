# 10 minute in, not super sure on ligc but taking a stab at it
# 20 min in, brute force solution without stack optimization
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)

        for i, e in enumerate(temperatures):
            for j in range(i+1, len(temperatures)):
                if e < temperatures[j]:
                    ret[i] = j - i
                    #print(ret)
                    break
            
        return ret
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([30,38,30,36,35,40,28]))


# [40, 40, 40, 40, 40, 40, 28]
# [30, 38, 38, 38, 38, 40, 40]