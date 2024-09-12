# solved in 40 mins from intuition, idk if this is the most efficent way
import heapq
from collections import defaultdict

from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap
        heap = []
        # counter dict:
        d = defaultdict(int)
        
        
        for t in tasks:
            d[t] += 1
        for index, key in enumerate(d):
            nextValidTime = 0
            heapq.heappush(heap, (d[key] * -1, key, nextValidTime)) 
        
        curTime = 0
        ret = []

        while len(heap) > 0:
            tempHeap = []
            pushedSomething = False
            while len(heap) > 0:
                cur = heapq.heappop(heap)
                occurance = cur[0] * -1 # stupid maxheap
                val = cur[1]
                onlyAfterThisTime = cur[2]

                if curTime >= onlyAfterThisTime:
                    ret.append(cur[1])
                    curTime += 1
                    occurance -= 1
                    onlyAfterThisTime += n+1 # this one off set is stupid but idk
                    pushedSomething = True
                
                if occurance > 0:
                    heapq.heappush(tempHeap, (occurance * -1, val, onlyAfterThisTime))

            if pushedSomething == False:
                ret.append(None)
                curTime += 1

            heap = tempHeap

        print(ret)
        print (len(ret))
        return len(ret)

    # def maxHeapPush(self, heap, v):
    #     heapq.heappush(heap, v * -1)
    #     return
    # def maxHeapPop(self, heap):
    #     return heapq.heappop(heap) * -1
    # def maxHeapPeak(self,heap):
        
        return heap[0] * -1

if __name__ == '__main__':
    sol = Solution()

    sol.leastInterval(["X","X","Y","Y"], 2) # 5
    sol.leastInterval(["A","A","A","B","C"], 3) # 9

'''
A A A B C D E F H I,3 #
'''


### It can't be this Max of cost common occurance * n , length


'''
A A A A B B B B , 4 #
'''