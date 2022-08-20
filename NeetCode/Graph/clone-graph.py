from pprint import pprint

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
    def cloneGraph(self, node: 'Node') -> 'Node':
        if (node == None):
            return None;

        q = []
        q.append(node)
        
        newNodes = {}
        
        while len(q) > 0:
            curNode = q.pop()
            newNode = Node(curNode.val, None)
            newNeighbors = []
            for i, neighbor in enumerate(curNode.neighbors):
                if (not neighbor.val in newNodes):
                    q.append(neighbor)
                newNeighbors.append(neighbor.val)
            newNodes[newNode.val] = {'neighbors': newNeighbors, 'node': newNode}
        
        #print(newNodes)
        
        
        for key, newNodeStruct in newNodes.items():
            print(newNodeStruct)
            
            for i, neighborVal in enumerate(newNodeStruct['neighbors']):
                print(neighborVal)
                newNode = newNodeStruct['node']
                if (newNode.neighbors == None):
                    newNode.neighbors = []
                neighborNode = newNodes[neighborVal]['node']
                newNode.neighbors.append(neighborNode)

                
        firstIndex = list(newNodes)[0]
        print('firstIndex')        
        
        return newNodes[firstIndex]['node'] if len(newNodes) > 0 else None

'''
[[2,4],[1,3],[2,4],[1,3]]
[[]]
[]
'''
