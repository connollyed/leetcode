# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        sum = 0
        if root == None:
            return sum

        if root.val <= high and root.val >= low:
            sum += root.val
        
        if root.left != None and root.val >= low: 
            sum += self.rangeSumBST(root.left, low, high)
        if root.right != None and root.val <= high:
            sum += self.rangeSumBST(root.right, low, high)
            
        return sum
    
# ADDED check to ensure value is range