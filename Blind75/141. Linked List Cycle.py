# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        """
        Approach 1
        """

        #         visited = set()
        #         curr = head
        #         while curr:
        #             if curr in visited:
        #                 return True
        #             visited.add(curr)
        #             curr = curr.next
        #         return False
        # Time = O(N), Space = O(N)

        """
        Approach 2
        """
        # Floyd's Cycle Finding Algorithm
        # --> Time = O(N), Space = O(1)

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
