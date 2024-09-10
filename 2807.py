# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getGCD(a, b):
            return b == 0 and a or getGCD(b, a % b)

        cur = head
        while cur:

            if cur.next is None:
                break

            newNode = ListNode(getGCD(cur.val, cur.next.val), cur.next)
            cur.next = newNode

            cur = cur.next.next

        return head