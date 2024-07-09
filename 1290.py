# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        cur = head

        val = 0
        while cur is not None:
            val = val << 1
            val = val | cur.val 
            cur = cur.next

        return val