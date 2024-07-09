# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        n_paths = []
        stack = []

        stack.append([root, str(root.val)])
        
        while len(stack) > 0:
            cur, path  = stack.pop(-1)

            if cur.left == None and cur.right == None:
                n_paths.append(path)
                print(n_paths)

            if cur.left:
                stack.append([cur.left, path + "->" + (str(cur.left.val))])
            if cur.right:
                stack.append([cur.right, path + "->" + (str(cur.right.val))])

        return n_paths