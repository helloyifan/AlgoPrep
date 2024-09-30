from typing import List
import copy
# Tried for 40 mins, understood that we have to find a cycle in this graph,
# But not sure how to deal with actually building the ordered list

# Solved it in another 20, but needed to watch neetcode vide
# basically split it into 2 sub problems
# 1. Detect if there is a cycle in single directioend  graph
    # - you do this by steping through each node to see if theres a cycle with each node
# 2. To build a topological sort, you need to explore all the child nodes before you can add it into you results
    # - in addition, i also have to do that for each node incase the nodes are not attached to a graph

# This solution is correct, but not efficient enough to pass on LC
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # node via adjaceny list?
        nodes = {}
        
        for i in range(numCourses):
            nodes[i] = []
        for e in prerequisites:
            nodes[e[0]].append(e[1])
 
        history = []
        #print(nodes)

        cycleDetected = self.dfsCycleDetection(nodes)
        if cycleDetected:
            history = []
        else:
            self.dfsToBuildHistory(nodes, history)
        
        print(history)
        return history
    
    def dfsCycleDetection(self, nodes):
        def helper(node, visited):
            if node in visited:
                return True

            neighbors = nodes[node]
            visited.append(node)
            for neighbor in neighbors:
                temp = helper(neighbor, visited)
                if temp == True:
                    return True
            visited.remove(node)
            return False
     
        for node in nodes:
            temp = helper(node, [])
            if temp == True:
                return True
        return False


    def dfsToBuildHistory(self, nodes, history):
        def helper(node):
            neighbors = nodes[node]
            if len(neighbors) == 0:
                if node not in history:
                    history.append(node)
                return

            for neighbor in neighbors:
                helper(neighbor)

            if node not in history:
                history.append(node)
            return
        for node in nodes:
            helper(node)
        return

sol = Solution()

sol.findOrder(3, [[1,0]])
sol.findOrder(3, [[0,1],[1,2],[2,0]])
sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])