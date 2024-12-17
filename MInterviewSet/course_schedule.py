# Note: Traverse through DFS  
# VISITED: MEANS WE HAVE FULLY TRAVERSED THIS NODE AND CAN GUARANTEE THERES NO CYCLES
# VISITEDl: IN THE MIDDLE OF OUR TRAVERSAL CYCLE DETECTED

# TC: O(n + p): where n is the numcourse and p is the number of prereqsuites
# For dfs we also use call stack which can be at most O(n) so in total its O(n+p)
# SC: O(n + p): for the  adj list

class DFSSolution:        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}
        for n in range(numCourses):
            adjList[n] = [] 
        for p in prerequisites:
            adjList[p[0]].append(p[1])
        
        print(adjList)

        VISITING = 1
        VISITED = 2

        def dfs(node, adjList, visited):
            
            if node in visited:
                if visited[node] == VISITING: #CYCLE DETECED
                    return False
                elif visited[node] == VISITED: # FULLY EXPLORED ALREADY
                    # Returning True indicates that this node is "safe" 
                    # (no cycles originate from it), and you don’t need to explore it further
                    return True

            visited[node] = VISITING

            for neighbor in adjList[node]:
                tempRet = dfs(neighbor, adjList, visited)
                if tempRet == False:
                    return False

            visited[node] = VISITED
            return True

        for i in range(numCourses):
            ret = dfs(i, adjList, {})
            if ret == False:
                return False
        return ret


# Notes: 
# KAHNS ALGORITHMS, TOPOLOGICAL SORT
# Indegree: Keep track of incoming edges to signal unblockage when 0
# AdjList: to keep track of edges (entry means taking X means you are partially unblocking elements in adjList[X])
# BFS to process
# THIS SOLUTION IS TOPOLOGICALLY SORTED AS A SIDE EFFECT :)!


# Complexity analysis: Use V E for graph questions
# TC: Building adjList is O(V+E) and indegree is O(V), BFS is O(E) total is O(V+E) V = numCourse, E = num of prerequisites
# SC: AdjList is O(V+E), inDegree is O(V) total is O(V+E)
from typing import List
from collections import defaultdict
class BFSSolution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(dict)

        # Track the number of prerequisites (incoming edges) for each course
        inDegree = [0 for _ in range(numCourses)] 

        for n in range(numCourses):
            adjList[n] = {}

        for p in prerequisites:
            targetCourse = p[0]
            prereqCourse = p[1]
            adjList[prereqCourse][targetCourse] = True # key is TO, value is FROM
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
