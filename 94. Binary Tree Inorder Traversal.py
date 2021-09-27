# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Binary Tree - order - root
        # pre-order : root - left - right
        # in-order  : left - root - right
        # post-order: left - right - root

        # D&C: subtree -> root

        """
              1
               \
                2
               /
              3

        input  pre-order        [1, null, 2, 3]
        output in-order         [1, 3, 2]

        """

        """
        Approach 1: recursion
        Time = O(N)  T(n) = 2T(n/2) + 1 -> O(N); Space = O(N)
        """

        #         result = []
        #         self.helper(root, result)
        #         return result

        #     def helper(self, root, result):
        #         if root:
        #             if root.left:
        #                 self.helper(root.left, result)
        #             result.append(root.val)
        #             if root.right:
        #                 self.helper(root.right, result)

        """
        syntax sugar
        """
        # if not root:
        #     return []
        # res = []
        # res += self.inorderTraversal(root.left)
        # res.append(root.val)
        # res += self.inorderTraversal(root.right)
        # return res

        """
        Approach 2: iteration with stack
        """
        # Time = O(N), Space =O(N) if generate new tree, otherwise O(1)
        # Stack - FILO

        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result

        """
        Approach 3: 
        """

        # Approach 3 - Morris Traversal
        # todo Morris Traversal - syntax bug
        # res = []
        # curr = root
        # pre = None
        # while root:
        #     if root.left is None:
        #         res.append(curr.val)
        #         curr = curr.right
        #     else:
        #         pre = curr.left
        #         while pre.right:
        #             pre = pre.right
        #         pre.right = curr
        #         temp = curr
        #         curr = curr.left
        #         temp.left = None
        # return res



