from typing import List

# I hate this question
# BFS approach
# We only add to the q after figureing out all the places we can just to from the previous step
# Count up the step by one



class Solution:
    def jump(self, nums: List[int]) -> int:
        q = []
        visited = [False] * len(nums) 
        q.append(0)
        steps = 0
        level_q = [] #only copy the stuff from level_q to q when q is empty, used to represent the idea of levels (one step per level)

        while len(q) > 0:
            print(q)
            headIndex = q.pop(0)

            ## Fail fast scenario
            if (headIndex >= len(nums) -1 ):
                return steps #not adding 1 because the current index is the final spot
            
            headVal = nums[headIndex]

            for i in range(1, headVal + 1):
                toAddIndex = headIndex + i
                print(toAddIndex)
                if (toAddIndex >= len(nums) -1 ):
                    return steps + 1 #adding 1 bcuz we are saying the next index is the final spot
                if (visited[toAddIndex] == False): # only add the index into the q if we havn't been there b4
                    level_q.append(toAddIndex)
                    visited[toAddIndex] = True # if first time we can jump to this node, mark it as visited (can probably use a set)

    
            if (len(q) == 0 ):
                print('level_q: ', level_q)
                q = level_q.copy()
                level_q = []
                # Take a step after visitiing all we can at this level
                steps +=1
        return -1

s = Solution()

# nums = [2,3,1,1,4]
# r = s.jump(nums)
# print('r',r) #2

# nums2 =[4,1,1,3,1,1,1]
# r2 = s.jump(nums2)
# print(r2) 

# nums4 = [2,3,3,0,0]
# r4 = s.jump(nums4)
# print('sol', r4)

# nums5 = [3,2,1]
# r5 = s.jump(nums5)
# print('sol', r5)

# nums6 = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
# r6 = s.jump(nums6)
# print('sol', r6)

nums7 = [0]
r7 = s.jump(nums7)
print('sol', r7)

'''
[4,2,1,0,4]
[2,3,3,0,0]
[3,2,1]
[2,3,1]
[4,1,1,3,1,1,1]
[1,1,1,1]
[1,3,2]
[0]
[5,9,3,2,1,0,2,3,3,1,0,0]
[10,9,8,7,6,5,4,3,2,1,1,0]
[5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
'''
