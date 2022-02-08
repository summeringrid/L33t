# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        columnTable = collections.defaultdict(list)  # mapping col to (row, node.val)
        min_col = max_col = 0

        def DFS(node, row, col):
            if node is not None:
                nonlocal min_col, max_col
                columnTable[col].append((row, node.val))

                min_col = min(min_col, col)
                max_col = max(max_col, col)

                DFS(node.left, row + 1, col - 1)
                DFS(node.right, row + 1, col + 1)

        DFS(root, 0, 0)

        res = []

        for c in range(min_col, max_col + 1):
            res.append([val for row, val in sorted(columnTable[c])])

        return res

    # DFS traversal: O(N)
    # O(N * log(N/k)), sort the columnTable (hashmap)
    # --> Overall Time = O(N * log(N/k))
    # Space = O(N)