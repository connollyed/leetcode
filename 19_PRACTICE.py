# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        behind = dummy
        cur = head

        i = 1
        while i<n and cur is not None:
            #print(f"getting place {cur.val}")
            cur = cur.next
            i += 1 

        print(f"CURRENTLY AT {cur.val}")

        while cur.next is not None:
            #print(f"cur = {cur.val} behind = {behind.val}")
            
            behind = behind.next
            cur = cur.next


        #print(f"AT THE END cur = {cur.val} behind = {behind.val}")
        behind.next = behind.next.next
        return dummy.next

        # TRICK IS DUMMY NODE