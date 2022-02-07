"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        head, cur = None, None

        def inorder(node):
            nonlocal head, cur
            # left
            if node.left: inorder(node.left)

            # node
            if cur:
                node.left = cur
                cur.right = node
            if not head:
                head = node
            cur = node

            # right
            if node.right: inorder(node.right)

        inorder(root)  # cur pointer reaches the last node
        cur.right = head
        head.left = cur
        return head

        # Time = O(n), Space = O(n)
