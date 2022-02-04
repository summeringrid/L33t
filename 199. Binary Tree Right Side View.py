# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS traverse the tree, append rightmost node to the res

        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):  # update the rightSide
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)

        return res

        # Time = O(N), Space = O(N)

    # more neater style:  HINT: don't forget the corner case!!
        if not root: return []
        res = []
        q = collections.deque([root])

        while q:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()

                if i == level_len - 1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

        # Time = O(N), Space = O(N)