# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot.left) or
                self.isSubtree(root.right, subRoot.right))

    def isSameTree(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.isSameTree(self, s.left, t.left) and
                    self.isSameTree(self, s.right, t.right))
        return False

    # Time = O(S*T), S is node num of the Tree root, T is node num of the Tree subRoot
    # Space = O(1)