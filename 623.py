# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            dummy = TreeNode(val, root, None)
            return dummy

        nodes_level = [(root,1)]

        while len(nodes_level) > 0:
            cur_node, cur_depth = nodes_level.pop(0)

            if cur_depth+1 == depth:
                # insert new left node and fix assignments
                newNode_LEFT = TreeNode(val, cur_node.left, None)
                cur_node.left = newNode_LEFT

                # insert new right node and fix assignments
                newNode_RIGHT = TreeNode(val, None, cur_node.right)
                cur_node.right = newNode_RIGHT

            elif cur_depth < depth:
                if cur_node.left is not None:
                    nodes_level.append((cur_node.left, cur_depth+1))
                if cur_node.right is not None:
                    nodes_level.append((cur_node.right, cur_depth+1))

        return root
