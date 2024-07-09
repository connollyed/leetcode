# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        prev_level = 1
        queue = [(root,prev_level)]

        total_list = []
        total = 0
        while len(queue) > 0:
            cur_node, cur_level = queue.pop(0)

            if cur_node is None:
                continue

            print(cur_node.val, cur_level)

            if cur_level != prev_level:
                total_list.append(total)
                total = cur_node.val
                prev_level = cur_level
            else:
                total += cur_node.val

            queue.append((cur_node.left, cur_level + 1))
            queue.append((cur_node.right, cur_level + 1))

        total_list.append(total)

        total_list.sort()
        
        if len(total_list) < k:
            return -1
        else:
            return total_list[-k]
        


# redone with DEQUE which is quicker

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        prev_level = 1
        queue = deque([(root,prev_level)])

        total_list = []
        total = 0
        while len(queue) > 0:
            cur_node, cur_level = queue.popleft()

            if cur_node is None:
                continue

            print(cur_node.val, cur_level)

            if cur_level != prev_level:
                total_list.append(total)
                total = cur_node.val
                prev_level = cur_level
            else:
                total += cur_node.val

            queue.append((cur_node.left, cur_level + 1))
            queue.append((cur_node.right, cur_level + 1))

        total_list.append(total)

        total_list.sort()
        
        if len(total_list) < k:
            return -1
        else:
            return total_list[-k]