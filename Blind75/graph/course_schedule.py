# Tried for 20mins got stuck
# Tried some more, this solution works but is too slow

# Tosolve: add memoization (if you know a course is cycle less, store it and look itup)

# Added memoization in 5 mins
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.adjacencyListDict = {} # {1 : {0: True}}, this means to take 1 you need 0
        # Iterate through this adjacencyListDict to check for cycles
        
        # Naivly add memoization
        self.memoization = {}

        # Setup all the courses
        for courseName in range(numCourses):
            self.adjacencyListDict[courseName] = []
        
        # Fill in the pre reqs
        for p in prerequisites:
            courseName = p[0]
            preReq = p[1]
            self.adjacencyListDict[courseName].append(preReq)
        
        for key, value in self.adjacencyListDict.items():
            tempRet = self.helper(key, [])
            if tempRet == False:
                return False
        return True
    
    # We need a helper that checks for cycle on head
    # The problem is that heads neighours could have multiple branches
     
    def helper(self, head, visited):
        if head in self.memoization:
            return True
        elif head in visited:
            return False
        
        visited.append(head)
        preReqs = self.adjacencyListDict[head]
        
        for preReq in preReqs:
            curFlag = self.helper(preReq, visited[:])
            if curFlag == False:
                return False

        self.memoization[head] = True
        return True
    
if __name__ == '__main__':
    s = Solution()
    # print(s.canFinish(2, [[1,0]]))
    # print(s.canFinish(2, [[1,0], [0,1]]))
    print(s.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))