# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=head)
        prev = dummy

        while head and head.next:
            l, r = head, head.next

            # swapping
            prev.next = r
            l.next = r.next
            r.next = l

            # pipeline the pointers
            prev = l
            head = l.next
        return dummy.next

    # Time = O(N)
    # Space = O(1)