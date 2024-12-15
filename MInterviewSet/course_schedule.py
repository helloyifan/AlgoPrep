# Notes: 
# Indegree: Keep track of incoming edges to signal unblockage when 0
# AdjList: to keep track of edges 
# BFS to process

# Complexity analysis: Use V E for graph questions
# TC: Building adjList is O(V+E) and indegree is O(V), BFS is O(E) total is O(V+E)
# SC: AdjList is O(V+E), inDegree is O(V) total is O(V+E)
from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(dict)

        # Track the number of prerequisites (incoming edges) for each course
        inDegree = [0 for _ in range(numCourses)] 

        for n in range(numCourses):
            adjList[n] = {}

        for p in prerequisites:
            targetCourse = p[0]
            prereqCourse = p[1]
            adjList[prereqCourse][targetCourse] = True
            inDegree[targetCourse] +=1
        
        # Subtract course from prereq list in BFS fashion
        # First remove courses that we can take already
        q = []

        for i, e in enumerate(inDegree):
            if e == 0:
                q.append(i) # can take i in indegree is 0 (no blockers)


        # Remove the courses we can take from the set
        # and remove other lists of prereq
        courseThatWeCanTake = set()

        while len(q) > 0:
            curPreReqCourse = q.pop()
            courseThatWeCanTake.add(curPreReqCourse)

            # Check to see what nodes we free up by cleaning this edge
            for neighbor in adjList[curPreReqCourse]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor]  == 0:
                    q.append(neighbor)
            del adjList[curPreReqCourse] # redundant but to show we remove the prereq record

        #print(adjList)
        #print('courseThatWeCanTake: ', courseThatWeCanTake)

        if len(courseThatWeCanTake) == numCourses:
            return True
        return False

sol = Solution()
print(sol.canFinish(2, [[1,0]]))
print(sol.canFinish(2, [[1,0],[0,1]]))