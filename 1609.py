# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:     
        queue = []

        level = 0
        queue.append((root, level))
        prev = float('-inf')
        while len(queue) > 0:

            # remove from front of queue
            cur_node, cur_level = queue.pop(0)
    
            print(f"{cur_node.val} and {cur_level}")

            
            
            # check if we are on new level
            if cur_level != level:
                level += 1
                if level % 2 == 0:
                    prev = float('-inf')
                else:
                    prev = float('inf')
            
            if level % 2 == 0:
                if prev >= cur_node.val:
                    print(f"EVEN LEVEL SHOULD BE DECREASING prev = {prev} > val {cur_node.val}")
                    return False
            else:
                if prev <= cur_node.val:
                    print(f"ODD LEVEL SHOULD BE INCREASING prev = {prev} > val {cur_node.val}")
                    return False
            
            prev = cur_node.val


            if level % 2 == cur_node.val % 2:
                return False

            if cur_node.left is not None:
                queue.append((cur_node.left, level + 1))
            
            if cur_node.right is not None:
                queue.append((cur_node.right, level + 1))

        return True
