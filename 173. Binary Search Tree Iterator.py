# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.order = []
        self._inOrder(root)
        self.index = -1

    def _inOrder(self, root):
        if not root: return
        self._inOrder(root.left)
        self.order.append(root.val)  # HINT: append val
        self._inOrder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.order[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.order)

    # Time = O(N), next: O(1), hasNext: O(1)
    # Space = O(N)

    # Optimized Space --> implement the recursion by using a stack

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmostOrder(root)

    def _leftmostOrder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        topmost = self.stack.pop()
        if topmost.right:
            self._leftmostOrder(topmost.right)
        return topmost.val  # HINT: return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    # Time = O(1), next/hasNext = O(1)
    # Space = O(N)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()