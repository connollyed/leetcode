# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        values = []

        def inorder(node):
            if node is None:
                return None

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
            return

        inorder(root)
        #print(values)


        def buildBST(l,r):
            if l <= r:
                mid = (l + r) // 2

                left_node  = buildBST(l,mid-1)
                right_node = buildBST(mid+1,r)

                return TreeNode(values[mid], left_node, right_node)

            return None

        return buildBST(0,len(values)-1)