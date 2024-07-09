# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rec(node):

            if node is None:
                return 0
            
            
            double = rec(node.next) + (node.val * 2)
            node.val = double % 10
            #print(node.val)
            return double // 10 # carry
                
        carry = rec(head)
        if carry != 0:
            new_head = ListNode(carry, head)
            new_head.next = head
            return new_head

        return head