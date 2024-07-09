# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = even = ListNode()
        odd_head = odd = ListNode()

        cur = head
        i = 0
        while cur is not None:
            if i % 2 == 0:
                even.next = cur
                even = even.next
                #even.next = None
            else:
                odd.next = cur
                odd = odd.next
                #odd.next = None
            
            i += 1
            cur = cur.next
        
        odd.next = None
        even.next = odd_head.next
        
        #return odd_head.next
        return even_head.next