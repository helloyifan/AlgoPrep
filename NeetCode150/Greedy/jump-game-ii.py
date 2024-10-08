from typing import List
# I guess the logic is that since is a greedy type question
# It wont make sense ver to not take the most you can take

# Attempt 1 took 35min ,not a good solution and required alot of debugging, way too complicated
class Solution:
    def jump(self, nums: List[int]) -> int:
        lastSpot = len(nums) -1
        curSpot = 0
        
        jumps = 0
        while curSpot < lastSpot:
            currentOptions = nums[curSpot]
            curMax = 0
            curMaxStepsToTake = 0

            for stepToTake in range(1, currentOptions + 1):
                iteratorIndex = curSpot + stepToTake
                
                if iteratorIndex == len(nums) -1:
                    curMaxStepsToTake = stepToTake
                    break
                elif iteratorIndex < len(nums):
                    maxDistanceAtCurrentI = nums[iteratorIndex] + stepToTake
                    if maxDistanceAtCurrentI >= curMax:
                        curMax = maxDistanceAtCurrentI
                        curMaxStepsToTake = stepToTake

            curSpot += curMaxStepsToTake
            print("curMaxStepsToTake: ", curMaxStepsToTake, "curSpot: ", curSpot)

            jumps += 1

        print(jumps)
        return jumps

sol = Solution()
sol.jump([2,4,1,1,1,1]) # 2
sol.jump([2,1,2,1,0]) # 2
sol.jump([2,1]) # 1 
sol.jump([2,3,1]) # 1