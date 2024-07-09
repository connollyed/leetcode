# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        key = root.val

        def dfs(node, key):
            print(f"val:{node.val} and key:{key}")

            if node.val != key:
                return False
            
            ret_left, ret_right = True, True
            if node.left is not None:
                ret_left = dfs(node.left, key)
            if node.right is not None:
                ret_right = dfs(node.right, key)

            return ret_left and ret_right
        
        return dfs(root,key)
        