# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1.Recursion Approach
        # if not root:
        #     return 0
        # else:
        #     leftHeight = self.maxDepth(root.left)
        #     rightHeight = self.maxDepth(root.right)
        #     return max(leftHeight, rightHeight) + 1

        # Syntax Sugar
        # return max(map(self.maxDepth, [root.left, root.right])) + 1 if root else 0

        # Time = O(N)
        # Space = O(N)
        # ↑ cuz in the worst case the tree is completely unbalanced,
        # then the recursion will occur N time (Height of the tree),
        # therefore the storage to keep the call stack would be O(N)

        # so the recurssive approach's space complexity is bound with the stack call
        # the tree traverse memory is relevant to the tree's height and the worst case is the linear tree

        # 2. Iteration (Stack)
        # Time = O(N), Space = O(logN) average

        stack = []
        if root:
            stack.append([1, root])

        depth = 0
        while stack != []:
            curr_depth, root = stack.pop()
            if root:
                depth = max(depth, curr_depth)
                stack.append((curr_depth + 1, root.left))
                stack.append((curr_depth + 1, root.right))

        return depth

