# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # parent pointer to find it

        # Approach I: parent Node ===============================================================

        # traverse the tree by using a parent pointer to find its ancestors
        # hashmap -> parent node

        stack = []
        stack.append(root)
        parent = {root: None}

        while p not in parent or q not in parent:   # until I find both p & q in the parent

            if stack:
                cur = stack.pop()

                if cur.left:
                    parent[cur.left] = cur
                    stack.append(cur.left)

                if cur.right:
                    parent[cur.right] = cur
                    stack.append(cur.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]       # traverse upward

        return q

        # Time = O(n)
        # Space = O(n)

        # Approach II recursive call ===============================================================
        def recursive_traverse(cur_node):

            if not cur_node:
                return False

            left = recursive_traverse(cur_node.left)
            right = recursive_traverse(cur_node.right)

            mid = cur_node == p or cur_node == q

            if mid + left + right >= 2:
                self.ans = cur_node

            return mid or left or right  # return True (any of these three values)

        recursive_traverse(root)
        return self.ans


        # Approach III recursion ===============================================================
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:  # both left and right exist, return root
            return root

        LCA = left if left else right
        return LCA





