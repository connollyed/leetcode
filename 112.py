# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False

        def dfs(node, total):
            total += node.val

            print(f"{node.val} and {total}")
            if node.right is None and node.left is None:
                if total == targetSum:
                    return True

            else:
                left_path = False
                right_path = False
                if node.left:
                    left_path = dfs(node.left, total)
                if node.right:
                    right_path = dfs(node.right, total)
            
                return left_path or right_path
        
        return dfs(root,0)