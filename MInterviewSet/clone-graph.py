# Notes:
# For DFS, create note, on backtrack add neighbors
# because during backtrack all the nodes exist in clonedDict

# TC: O(v+e): We traverse through every node and edge once to clone it
# SC: O(v+e) we copy every node and edge, we use O(v) space in call stack because we can go v vertex deep
# SC total is O(v+e)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class DFSSolution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clonedDict = {}

        def dfsCreateNodes(node, visited):
            if node == None:
                return

            if node.val in visited:
                return

            visited.add(node.val)
            clonedDict[node.val] = Node(val = node.val, neighbors = [])
            for n in node.neighbors:
                dfsCreateNodes(n, visited)
                clonedNeighbor = clonedDict[n.val] if n else None
                clonedDict[node.val].neighbors.append(clonedNeighbor) 

        dfsCreateNodes(node, set())
        
        ret = clonedDict[node.val] if node else None
        return ret
    

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# TC: O(v+e): We traverse through every node and edge once to clone it
# SC: O(v+e) we copy every node and edge

from typing import Optional
class BFSSolution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneDict = {}
        visited = set()
        q = deque([node])

        while len(q) > 0:
            tempQ = deque([])
            while len(q)>0:
                cur = q.pop()
                if cur == None or cur.val in visited:
                    continue # dont redo Nodes that have been processed

                # Processing
                visited.add(cur.val)
                if not cur.val in cloneDict:
                    cloneDict[cur.val] = Node(val=cur.val, neighbors = [])
                
                for n in cur.neighbors:
                    tempQ.appendleft(n)

                    if not n.val in cloneDict:
                        cloneDict[n.val] = Node(val=n.val, neighbors = [])

                    cloneDict[cur.val].neighbors.append(cloneDict[n.val])

            # Set q to be the tempQ we built
            q = tempQ

        ret = cloneDict[node.val] if node else None
        return ret