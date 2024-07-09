# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def inorder_helper( cur_node ):
            if cur_node == None:
                return

            inorder_helper(cur_node.left)
            print(cur_node.val)
            output.append(cur_node.val)
            inorder_helper(cur_node.right)
        
        inorder_helper( root )

        return output
