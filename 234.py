# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        vals = []
        cur = head
        while cur != None:
            vals.append(cur.val)
            cur = cur.next
        
        L = 0
        R = len(vals) - 1

        while L < R:
            if vals[L] != vals[R]:
                return False
            L+=1
            R-=1
        
        return True