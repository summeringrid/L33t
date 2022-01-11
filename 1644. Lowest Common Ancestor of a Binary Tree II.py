# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # [[TreeNode, pq_num],]
        def dfs(root, p, q):
            if not root:
                return (None, 0)
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if root == p or root == q:
                return (root, 1 + left[1] + right[1])

            if left[0] and right[0]:
                return (root, 2)

            LCA = left if left[0] else right

            return LCA

        res = dfs(root, p, q)
        if res[1] < 2:
            return None

        return res[0]
