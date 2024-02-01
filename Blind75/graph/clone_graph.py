# Completed in 20 mins
# Not sure if its even the optimal way based on what i can do

# I bascally traversed the graph twice,
#  once to create all the new Nodes
#  second time to connect the New Nodes, 
# im wondering if its possible to do it on pass


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.newNodeDict = {} 
        self.newFirstNode = None
        self.visitedForMapNode = {} # to make sure we only visit each node once to prevent cycles

        self.createNodes(node)
        self.mapNode(node)
        return self.newFirstNode

    def createNodes(self, node):
        if node == None:
            return 
        print(node.val)

        newNode = Node()
        newNode.val = node.val
        newNode.neighbors = [] # we assign neighbors in mapNode

        if self.newFirstNode == None:
            self.newFirstNode = newNode


        self.newNodeDict[node.val] = newNode

        for n in node.neighbors:
            if n.val not in self.newNodeDict:
                self.createNodes(n)
    
    def mapNode(self, node):
        if node == None:
            return 
        self.visitedForMapNode[node.val] = True
        newNode = self.newNodeDict[node.val]
        
        for n in node.neighbors:
            newNode.neighbors.append(self.newNodeDict[n.val])
            if n.val not in self.visitedForMapNode:
                self.mapNode(n)