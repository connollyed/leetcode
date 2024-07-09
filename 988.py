# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        smallest_string = "~"
        queue = [(root, "")]

        while (len(queue) > 0):
            cur_node, cur_string = queue.pop(0)

            cur_char = chr(ord('a') + cur_node.val)

            s = cur_string + cur_char

            if cur_node.left is None and cur_node.right is None:
                rev_s = s[::-1]
                smallest_string = min(smallest_string, rev_s)

            else:
                if cur_node.left is not None:
                    queue.append((cur_node.left, s))

                if cur_node.right is not None:
                    queue.append((cur_node.right, s))

        return smallest_string