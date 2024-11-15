# Q1. cheapest_flight (not the common leetcode one)

# find the cheapest departing and return flights 
# you can depart and return on samme date, but not return before depart
# index is date

# D [7,8,10,9,8]
# R [7,8,10,6,8]

# cheapest flight D[0] = 7, R[3] = 6 total is 13

# Time Complexity
# O(2n)
# space comeplxity
# O(n)
def cheapestFlight(D, R):
    preProcessR = [None for _ in range(len(R))]
    
    minVal = float('inf')
    for i in range(len(R)-1, -1 , -1):
        minVal = min(minVal, R[i])
        preProcessR[i] = minVal

    print(preProcessR)

    minFinalRet = float('inf')
    for i in range(len(D)):
        minFinalRet = min(D[i] + preProcessR[i], minFinalRet)

    print(minFinalRet)
    return minFinalRet

D = [7,8,10,9,8]
R = [7,8,10,6,8]
cheapestFlight(D, R)