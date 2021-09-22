# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            last = rightTail or leftTail or root
            return last

        dfs(root)

        # Time = O(N)
        # Space = O(N) which is occupied by the recursion stack

        # optimized solution
        """
        Recursion is all about postponing decisions until something else is completed.
        Use stack to postpone stuff. However, in order to get rid of the stack altogether:
        -> come up with a greedy way that will be costlier in terms of time but will be space-efficient
        """
        if not root:
            return None

        curr = root
        while curr:

            # If the curr node has a left child
            if curr.left:

                # Find the rightmost curr node
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                    # rightmost = 6
                    # curr.left = 2
                    # curr = 5

                # rewire the connections
                rightmost.right = curr.right
                curr.right = curr.left
                curr.left = None

            # move on to the right side of the tree
            curr = curr.right

        # Time = O(N) Space = O(1) boom!