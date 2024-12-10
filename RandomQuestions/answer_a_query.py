import heapq

def answer_a_query(N, Q, queries):
    h = []
    output = []
    for q in queries:
        curType = q[0]
        curIndex = q[1]

        # Set
        if curType == 1:
            heapq.heappush(h, curIndex)

        # Get
        elif curType == 2:
            backup = []
            # We want to find the first value large
            while len(h) > 0 and h[0] < curIndex:
                poppedVal = heapq.heappop(h)
                backup.append(poppedVal)
             
            if len(h) != 0 and h[0] >= curIndex:
                output.append(h[0])
            else:
                output.append(-1)

            # Repair heap
            h.extend(backup)

    print(output)
    return output

answer_a_query(5, 5, [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]])