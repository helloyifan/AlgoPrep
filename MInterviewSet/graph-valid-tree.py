# Notes: Used DFS on a bidriectional graph to see if we can find cycles or touch everything
# In a un-directed graph, we have to make sure we dont go back to paretn

# We dont need to keep track of VISITED vs VISITING, just VISITING is enough

# TC: O(e+v): We traverse through every edge and vertex in the worst case
# SC: O(e+v): We store every edge and vertex in

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for e in edges:
            adjList[e[0]].append(e[1]) # Graph is bidirectional
            adjList[e[1]].append(e[0])


        def dfs(node, adjList, visited, parent): # Bidirectional graph we need to keep track of parent
            if node in visited:
                if visited[node] == 1:
                    print('cycle deteced: ', node, visited)
                    return False #cycle detected

            visited[node] = 1 # visiting
            neighbor = adjList[node]

            for n in neighbor:
                if n == parent:
                    continue # skip parent
                temp = dfs(n, adjList, visited, node)
                if temp == False:
                    return False

            return True

        
        # check for cycles
        visited = defaultdict(int)
        # See if we can reach every node from parent?
        noCycles = dfs(0, adjList, visited, None)
        if noCycles == False:
            return False
        # Did we reach every node from 0?
        if len(visited) < n:
            return False

        return True