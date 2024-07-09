# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2

        cur = ListNode(0)
        sum_head = cur

        sum = 0
        carry = 0
        v1 = 0
        v2 = 0
        while ptr1 or ptr2 or carry:
            if ptr1:
                v1 = ptr1.val
            else:
                v1 = 0

            if ptr2:
                v2 = ptr2.val
            else:
                v2 = 0

            sum = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            
            cur.next = ListNode(sum)
            cur = cur.next

            if ptr1:
                ptr1 = ptr1.next
            
            if ptr2:
                ptr2 = ptr2.next

        return sum_head.next