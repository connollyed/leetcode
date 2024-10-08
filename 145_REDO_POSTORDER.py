# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if root == None:
            return
        

        if root.left != None:
            res.extend(self.postorderTraversal(root.left))
        
        if root.right != None:
            res.extend(self.postorderTraversal(root.right))
        
        res.append(root.val)
        return res