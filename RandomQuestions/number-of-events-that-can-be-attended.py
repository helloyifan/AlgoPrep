# 40min attempt 1 (failed so hard)
# 40min attempt 2 (hella debugging after reading answer)

# Time comp:
# O(nlogn) for sort
# O(d) where d is the last day of event
# O(n) each event we add to heapq at some point
# O(n) each event remove from heapq at some point
# Total O(nlogn + d)

# Space complexity
# O(n) wher each event is added to heap in worst case
import heapq
 
class Solution:
    def maxEvents(self, events):
        events.sort(key = lambda k:k[0])

        lastDay = 0
        for event in events:
            lastDay = max(lastDay, event[1])

        h = []
        d = 0
        included = 0
        conferencesAttended =0 
        
        while d <= lastDay:
            # Step 1. add events you can now go to
            while included < len(events) and d >= events[included][0]:
                curEvent = events[included]
                eventToAdd = (curEvent[1], curEvent[0])  #(enddate, startdate)
                #print("Added: ", eventToAdd)
                heapq.heappush(h, eventToAdd)
                included += 1

            # Step 2. cleanup events that have already ended
            while len(h) > 0 and h[0][0] < d: # if the head of heap, has a end date that has passed
                expired = heapq.heappop(h)
            # Step 3. attend one
            if len(h) > 0 and h[0][1] <= d: # if the head of heap, has a start date thats today or earlier
                attended = heapq.heappop(h)
                conferencesAttended += 1
                # print(d, "attended: ", attended)
            # else:
            #     print(d, "There wasnt one that we could attend today" )

            d += 1
        
        #print(h)
        # print('included: ', included)
        # print('d: ', d)

        #print("conferencesAttended:", conferencesAttended)
        #print('---')
        return conferencesAttended
    
sol = Solution()
# sol.maxEvents([[1,2],[2,3],[3,4],[1,2]]) # 4
# sol.maxEvents([[1,2],[2,3],[3,4]]) # 3
# sol.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]) #4
# sol.maxEvents([[1,10],[2,2],[2,2],[2,2],[2,2]]) #2

sol.maxEvents([
    [27,29],[28,32],[3,3]  ,[24,25],[7,7],
    [22,25],[14,15],[13,17],[1,2]  ,[7,7],
    [10,12],[9,13] ,[21,25],[20,21],[20,22],
    [19,20],[27,28],[9,9]  ,[21,24],[18,21],
    [6,10] ,[29,30],[22,24]
]) #21