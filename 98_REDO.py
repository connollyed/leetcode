# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        lower = float("-inf")
        upper = float("inf")

        def dfs(node , lower, upper):
            if node is None:
                return True

            if not (node.val < upper and node.val > lower):
                    return False

            return (dfs(node.left, lower, node.val) and 
                    dfs(node.right,node.val,upper))

        return dfs(root, lower, upper)