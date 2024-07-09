# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:  
        cur = list1

        a_ptr = None
        count = 0
        while count < a:
            a_ptr = cur
            cur = cur.next
            count += 1

        b_ptr = None
        while count <= b+1:
            b_ptr = cur
            print(f"b_ptr: {b_ptr.val}")
            cur = cur.next
            count += 1
        # here we have a and b

        

        a_ptr.next = list2
        l2 = list2
        while l2.next is not None:
            l2 = l2.next

        l2.next = b_ptr

        return list1