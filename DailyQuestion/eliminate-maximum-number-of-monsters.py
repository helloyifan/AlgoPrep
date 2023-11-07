from typing import List
import math 

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        lose_turn = [None] * len(dist)
        
        # I wanna get a list of at which turn i will lose for each monster

        for i, e in enumerate(dist):
            turns_until_lose = math.ceil(e / speed[i])
            lose_turn[i] = turns_until_lose

        # After getting a list of which turn i will lose, I will figure out how far i can get with that list 
        lose_turn.sort()
        turn_counter = 0
        for i, e in enumerate(lose_turn):
            if (e <= turn_counter):
                break # early loss
            turn_counter += 1

        return turn_counter




sol = Solution()

dist = [1,3,4]
speed = [1,1,1]
print(sol.eliminateMaximum(dist, speed))

# dist2 = [1,1,2,3]
# speed2 = [1,1,1,1]

# print(sol.eliminateMaximum(dist2, speed2))


# dist3 = [3,2,4]
# speed3 = [5,3,2]
# print(sol.eliminateMaximum(dist3, speed3))

# dist4 = [5,2,4]
# speed4 = [5,5,2]
# print(sol.eliminateMaximum(dist4, speed4))

# dist5 = [4,2,8]
# speed5 = [2,1,4]
# print(sol.eliminateMaximum(dist5, speed5))

dist6 =[46,33,44,42,46,36,7,36,31,47,38,42,43,48,48,25,28,44,49,47,29,32,30,6,42,9,39,48,22,26,50,34,40,22,10,45,7,43,24,18,40,44,17,39,36]
speed6 = [1,2,1,3,1,1,1,1,1,1,1,1,1,1,7,1,1,3,2,2,2,1,2,1,1,1,1,1,1,1,1,6,1,1,1,8,1,1,1,3,6,1,3,1,1]
print(sol.eliminateMaximum(dist6, speed6))
