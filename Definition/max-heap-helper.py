class maxHeapUtil:
    def maxHeapify(lst):
        for i in range(0, len(lst)):
            lst[i] = lst[i] * -1
        heapq.heapify(lst)

    def maxheappush(heap, item):
        heapq.heappush(heap, item * -1)

    def maxheappop(heap):
        return heapq.heappop(heap) * -1
