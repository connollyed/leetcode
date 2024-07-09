# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(node):
            if node.val == 0:
                return False
            if node.val == 1:
                return True

            if node.val == 2:
                return bfs(node.left) or bfs(node.right)
            if node.val == 3:
                return bfs(node.left) and bfs(node.right)

        return bfs(root)
