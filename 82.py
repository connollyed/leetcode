# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode()
        new_head.next = head
        
        prev = new_head
        cur = head

        while(cur):
            duplicate_found = False

            while(cur.next is not None and (cur.val == cur.next.val)):
                duplicate_found = True
                cur = cur.next

            if duplicate_found:
                prev.next = cur.next
            else:
                prev = prev.next

            #print(f"{cur.val}, {next.val}")
            cur = cur.next
            
        return new_head.next