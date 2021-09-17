# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        # curr.next= l1 if l1 is not None else l2
        curr.next = l1 or l2

        return dummy.next

    # Time = O(n+m), Space = O(1)
    # The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
