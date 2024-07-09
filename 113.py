# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root is None:
            return []


        ret_list = []
        def dfs(node, values):
            values.append(node.val)

            if node.left is None and node.right is None:
                # check its target
                if sum(values) == targetSum:
                    ret_list.append(list(values))
            else:
                if node.left is not None:
                    dfs(node.left, list(values))
                    #values.pop(-1)
                
                if node.right is not None:
                    dfs(node.right, list(values))
                    #values.pop(-1)

                return
        
        
        dfs(root, [])
        return ret_list