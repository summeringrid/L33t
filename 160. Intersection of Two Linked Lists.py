# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur = headA
        A_set = set()
        while cur:
            A_set.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in A_set:
                return cur
            else:
                cur = cur.next
        return None
