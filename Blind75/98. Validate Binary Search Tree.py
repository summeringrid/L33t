# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(node, leftBound, rightBound):
            if not node:
                return True
            if not (node.val > leftBound and node.val < rightBound):
                return False

            return (validBST(node.left, leftBound, node.val) and
                    validBST(node.right, node.val, rightBound))

        return validBST(root, float('-inf'), float('inf'))