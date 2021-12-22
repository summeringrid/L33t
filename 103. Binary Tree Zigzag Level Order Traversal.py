# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        levels = []
        queue = deque([root])
        reverse = False

        while queue:
            level_len = len(queue)
            temp = [0] * level_len

            for i in range(level_len):
                currNode = queue.popleft()

                if not reverse:
                    temp[i] = currNode.val
                else:
                    temp[level_len - i - 1] = currNode.val

                if currNode.left:
                    queue.append(currNode.left)

                if currNode.right:
                    queue.append(currNode.right)

            reverse = not reverse
            levels.append(temp)

        return levels

    # Time = O(n), Space = O(n)