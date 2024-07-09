# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.ret = 0
        def dfs(node, isLeft):
            if isLeft == True and ((node.left is None) and (node.right is None)):
                self.ret += node.val
                return

            if node.left is not None:
                dfs(node.left, True)
            if node.right is not None:
                dfs(node.right, False)
            
            return


        if root.left is not None:
            dfs(root.left, True)
        if root.right is not None:
            dfs(root.right, False)


        return self.ret