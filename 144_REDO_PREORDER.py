# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if root == None:
            return res

        res.append(root.val)  # Append current node value before traversing left and right subtrees
        
        if root.left != None:
            res.extend(self.preorderTraversal(root.left))  # Extend the result with values from left subtree
            
        if root.right != None:
            res.extend(self.preorderTraversal(root.right))  # Extend the result with values from right subtree
        
        return res