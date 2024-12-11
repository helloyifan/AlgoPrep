# NOtes heap questions
# TC: O(nlogk) time (k is input)
# SC: O(k)

import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    
    # Steps 1.
    # for each point, we calculate E distance to (0,0) #O(n)
    h = []
    mh = []
    for p in points:

    # Step 2b.
    # We only need to store it in the heap some of the time O(n * logn)
        eDis = (math.sqrt(p[0]**2 + p[1]**2))
        heapq.heappush(h, (-eDis, p)) # This is log(k)
        
        # This makes sure heap is always size k
        if len(h) > k: 
            heapq.heappop(h)
        
    # Step 3.
    # We get the first K elements # O(1)
    ret = []
    for _ in range(k):
        point = heapq.heappop(h)
        ret.append(point[1])
        
    return ret