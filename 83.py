# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head

        while(cur is not None and cur.next is not None):
            #print(f"{cur.val}, {cur.next.val}")
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next

        return head