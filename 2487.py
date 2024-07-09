# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        cur = head

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        dummy_head = ListNode(-1)
        temp_prev, curr = dummy_head, prev
        # Traverse the reversed list, keeping nodes greater or equal to previous
        while curr:
            if curr.val >= temp_prev.val:
                temp_prev.next = curr
                temp_prev = curr
                curr = curr.next
            else:
                curr = curr.next
        temp_prev.next = None
        
        # Reverse the result list again
        new_prev = None
        curr = dummy_head.next
        while curr:
            curr.next, new_prev, curr = new_prev, curr, curr.next

        return new_prev