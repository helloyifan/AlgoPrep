# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Notes: preprocess a childParent relationship with DFS or BFS
# Aftewards traverse datastrucutre again with Target as root
# Consider childParent as a path to traverse

# TC: O(n) for preprocess, O(n) for traversal, total is O(n)
# SC: ChildParent has a node for everynode so it grows linearly O(n), 
# O(height) (height is logn) for call stack in balancced, O(n) in worse case
# O(n) for visited
# O(n) for ret
class DFSSolution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # First preprocess the tree to build childParent relation
        childParent = {}

        def dfsChildParentPreprocess(root, childParent):
            if root == None:
                return
            
            if root.left != None:
                childParent[root.left.val] = root
                dfsChildParentPreprocess(root.left, childParent)

            if root.right != None:
                childParent[root.right.val] = root
                dfsChildParentPreprocess(root.right, childParent)
            return

        ret = []
        def dfsDisKTraversal(root, childParent, visited, k):
            if root == None:
                return 
            # if in visited
            if root.val in visited:
                return 
            # if we are k away            
            if k == 0:
                ret.append(root.val)
                return 

            # Set Visited
            visited[root.val] = True

 
            dfsDisKTraversal(root.left, childParent, visited, k-1)
            dfsDisKTraversal(root.right, childParent, visited, k-1)

            if root.val in childParent: # Note actual root node has no parent
                dfsDisKTraversal(childParent[root.val], childParent, visited, k-1)
            
            # clean up back tracking
            del visited[root.val]

            return 

        dfsChildParentPreprocess(root, childParent)
        
        dfsDisKTraversal(target, childParent, {}, k)
        print(ret)
        return ret

# Notes: Basically same as above just BFS
# TC: O(n) for BFS to preprocess, O(n) to traverse
# SC: O(n) to build childParent
# O(n) for visited
# O(n) for ret

class BFSSolution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        childParent = {}

        # BFS to build childparent
        q = [root]
        while len(q) > 0:
            tempQ = []
            while len(q) > 0:
                cur = q.pop()
                if cur.left != None:
                    childParent[cur.left.val] = cur
                    q.append(cur.left)
                if cur.right != None:
                    childParent[cur.right.val] = cur
                    q.append(cur.right)
            q = tempQ

        # BFS to traverse
        ret = []
        q = [target]
        visited = {}
        counter =0
        while len(q) > 0:
            tempQ = []
            while len(q) > 0:
                cur = q.pop()
                
                if cur == None:
                    continue

                if cur.val in visited: # no need to go into a node we've been to 
                    continue

                if counter == k:
                    ret.append(cur.val)
                    continue # no need to keep going

                visited[cur.val] = True
            
                tempQ.append(cur.left)
                tempQ.append(cur.right)
                if cur.val in childParent:
                    tempQ.append(childParent[cur.val])
            q = tempQ
            counter +=1

        print(ret)
        return ret