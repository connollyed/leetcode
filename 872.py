# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        list1 = []
        list2 = []

        def dfs(cur_node, cur_list):
            if cur_node is None:
                return
            
            if cur_node.left is None and cur_node.right is None:
                cur_list.append(cur_node.val)
                return
            
            if cur_node.left is not None:
                dfs(cur_node.left, cur_list)
            if cur_node.right is not None:
                dfs(cur_node.right, cur_list)

            return

        dfs(root1, list1)
        dfs(root2, list2)
        return list1 == list2