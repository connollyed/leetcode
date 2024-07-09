# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(cur_node):
            if not cur_node :
                return 0
            return 1 + max(dfs(cur_node.left), dfs(cur_node.right)) # increment depth
        
        return dfs(root) # depth 
    


# Itterative BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0  

        queue = []
        queue.append(root)
        depth = 0


        while len(queue) > 0:
            depth += 1
            for i in range(len(queue)): # This is len of queue at current time i.e a level
                cur = queue.pop(0)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)

        return depth

        
    
# Itterative DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = 0
        
        if root == None:
            return 0

        stack = []
        stack.append([root,1])  # Stack = NODE, NODES_DEPTH = 1 at least 1 the root

        while len(stack) > 0:
            node, depth = stack.pop(-1)
            max_depth = max(max_depth, depth)

            if node.left != None:
                stack.append([node.left, depth+1])

            if node.right != None:
                stack.append([node.right, depth+1])

        return max_depth
