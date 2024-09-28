from typing import List

# Attempt1: spent 40mins, i dont think i understood the question becaiuse by my account its right
# I geuiinely dont know whats wrong with my solution

# Attempt2: Spent another 20 min on attempt 2, where i merge the stacks, but its the same issue as attemtp 1

# Attempt3: Spent 5 mins, Looked at answer, the issues whas my understanding that "the cars aren't moving in discrete steps"
# its moreso of a math solution where cars dont get there on the integer time mark

from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carFleets = []
        for i in range(0, len(position)):
            car = [position[i], speed[i]] # Pos, speed
            carFleets.append(car)

        carFleets.sort(key=lambda x: x[0], reverse = True)

        fleets = 0
        prevTimeToReach = 0 # 0 for base case, faster cars get there in less time

        for pos, speed in carFleets:
            remainingDistance = target - pos
            timeItWillTake = remainingDistance / speed
            print(timeItWillTake)

            # More time means slower car
            if timeItWillTake > prevTimeToReach:
                fleets += 1
                prevTimeToReach = timeItWillTake
        print(fleets)
        return fleets
     
    def attempt1(self, target: int, position: List[int], speed: List[int]) -> int:
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
    
    # merge different stacks together method , didnt work
    def attempt2(self, target: int, position: List[int], speed: List[int]) -> int:
        carFleets = []
        
        for i in range(0, len(position)):
            car = [position[i], speed[i]] # Pos, speed
            carFleets.append(car)

        carFleets.sort(key=lambda x: x[0], reverse = True)

        print(carFleets)
        ret = 0
        while len(carFleets) >0:
            tempFleet = []
            prevCarLoc = None
            
            while len(carFleets) > 0:
                curCarFleet = carFleets.pop(0)      
                curCarLoc = curCarFleet[0] + curCarFleet[1]
                curCarFleet[0] = curCarLoc
                
                print("prevCarLoc: ", prevCarLoc, "curCarLoc: ", curCarLoc)

                # Caught up (so join it together with the fleet infront... by not adding it)
                if prevCarLoc != None and prevCarLoc <= curCarLoc:
                    pass
                # Finished, if they caught up and finished at the same time, we dont count it
                elif curCarLoc >= target:
                    ret += 1
                # Didnt catch up
                else:
                    tempFleet.append(curCarFleet)


                if prevCarLoc == None or curCarLoc < prevCarLoc:
                    prevCarLoc = curCarLoc

            carFleets = tempFleet

            print('----',  ret)
        print(ret)
        return ret
    
   
        
sol = Solution()
# sol.carFleet(10, [1, 4], [3, 2]) # 1 
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# cycle 0: 1, 4
# cycle 1: 4, 6
# cycle 2: 7, 8
# cycle 3: 10, 10 (so multiple cars can be in the same fleet, but cant pass)


# sol.carFleet(10, [4,1,0,7], [2,2,1,1]) # 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

#sol.carFleet(10, [6, 8], [3, 2]) # 2

sol.carFleet(31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]) # 6
