# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        queue = [(root,0)]
        while len(queue) > 0:
            cur_node, cur_depth = queue.pop(0)

            if (max_depth < cur_depth):
                max_depth = cur_depth
                ret_val = cur_node.val
            
            if cur_node.left is not None:
                queue.append((cur_node.left, cur_depth + 1))
            
            if cur_node.right is not None:
                queue.append((cur_node.right, cur_depth + 1))

        return ret_val
        

