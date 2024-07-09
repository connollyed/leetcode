# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        global newNode

        ptr1 = list1
        ptr2 = list2

        output = ListNode()
        current = output

        while ptr1 != None and ptr2 != None:
            if ptr1.val > ptr2.val:
                current.next = ptr2
                ptr2 = ptr2.next 
            else:
                current.next = ptr1
                ptr1 = ptr1.next
            
            current = current.next

        if ptr1 != None: 
            current.next = ptr1
        elif ptr2 != None:
            current.next = ptr2

        return output.next
    


    # Notes can revise this
    # remove nones so its just prt1 and ptr2
    # if ptr1