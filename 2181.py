# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        total = 0
        first_run = True
        prev = None
        cur = head
        while cur is not None:
            if cur.val == 0:
                
                if first_run:
                    first_run = False
                    head = head.next
                    prev = head
                
                else:
                    newNode = ListNode(total,cur)
            
                    prev.next = newNode
                    prev = prev.next

                    prev.next = cur.next
                
                total = 0
                
            total += cur.val
            cur = cur.next

        return head.next