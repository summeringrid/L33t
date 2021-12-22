# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # implement a bfs

        # corner case:
        if not root:
            return []

        levels = []
        queue = deque([root])
        level = 0
        while queue:
            levels.append([])
            level_length = len(queue)

            for i in range(level_length):
                currNode = queue.popleft()
                levels[level].append(currNode.val)

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

            level += 1

        return levels

        # Time = O(n), Space = O(n)