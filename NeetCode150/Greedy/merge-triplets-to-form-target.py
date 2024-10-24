# Solved NC in 23 min with pure logic and instinct alone
# The idea is to iteate through the list for each number in the triplet, and passing/skipping if other two digits are too big
from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        for i, ei in enumerate(triplets):
            if ei[0] == target[0]:
                if ei[1] > target[1]:
                    continue
                if ei[2] > target[2]:
                    continue
                
                for j, ej in enumerate(triplets):              
                    if ej[0] > target[0]:
                        continue
                    if ej[2] > target[2]:
                        continue
                    
                    if ej[1] == target[1]:
                        for k, ek in enumerate(triplets):

                            if ek[0] > target[0]:
                                continue
                            if ek[1] > target[1]:
                                continue

                            if ek[2] == target[2]:
                                return True
                            else: # for k level
                                continue
                    else: # for j level
                        continue
            else: # for i level
                continue
        return False # Found nothing
    
    # def merge(self, trip1, trip2):
    #     ret = []
    #     for i in range(3):
    #         ret.append(max(trip1[i], trip2[i]))
    #     return ret
    
sol = Solution()
print(sol.mergeTriplets([[1,2,3],[7,1,1]], [7,2,3]))
print(sol.mergeTriplets([[2,5,6],[1,4,4],[5,7,5]], [5,4,6]))
print(sol.mergeTriplets([[3,5,1],[10,5,7]],[3,5,7]))

'''
[119] [191] [911] t=[999]

find if 9 exists in all 3 spots

if cond1 breaks cond2, then its not possible

'''