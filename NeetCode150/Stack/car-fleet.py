# spent 40mins, i dont think i understood the question becaiuse by my account its right
# I geuiinely dont know whats wrong with my solution
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars =  []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda car: car[0], reverse = True) #sort cars by starting location (in reverse)


        ret = 0
        while len(cars) > 0:
            print(cars)

            newStackOfCars = []
            curLeaderPos = None

            prevCarFinishedLocation = float('inf')
            while len(cars) >0:
                tempCar = cars.pop(0)
                tempCarNewLoc = tempCar[0] + tempCar[1]

                if curLeaderPos == None:
                    curLeaderPos = tempCarNewLoc
                    tempCar[0] = tempCarNewLoc
                elif tempCarNewLoc > curLeaderPos:
                    tempCar[0] = curLeaderPos
                elif tempCarNewLoc <= curLeaderPos:
                    curLeaderPos = tempCarNewLoc
                    tempCar[0] = tempCarNewLoc


                if tempCar[0] >= target:
                    print("finishers: ", tempCar)
                    if prevCarFinishedLocation > tempCar[0]:
                        prevCarFinishedLocation = tempCar[0]
                        ret += 1
                
                # only add car to new deck ikf it hasnt finished
                else:
                    newStackOfCars.append(tempCar)

            cars = newStackOfCars # reset stack of cars
        
        print(ret)
        return ret 

sol = Solution()
# sol.carFleet(10, [1, 4], [3, 2]) # 1 
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# cycle 0: 1, 4
# cycle 1: 4, 6
# cycle 2: 7, 8
# cycle 3: 10, 10 (so multiple cars can be in the same fleet, but cant pass)


#sol.carFleet(10, [4,1,0,7], [2,2,1,1]) # 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

#sol.carFleet(10, [6, 8], [3, 2]) # 1

sol.carFleet(31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]) # 6
