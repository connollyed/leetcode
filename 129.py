# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.total = 0
        def dfs(node, value):
            cur_value = value + str(node.val)
            if node.left is None and node.right is None:
                self.total += int(cur_value)
                return

            if node.left is not None:
                dfs(node.left, cur_value)
            
            if node.right is not None:
                dfs(node.right, cur_value)

        dfs(root, "")

        return self.total