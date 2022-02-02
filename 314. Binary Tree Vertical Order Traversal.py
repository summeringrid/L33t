# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS ==========================================================
        column_table = defaultdict(list)        # mapping column to the node
        queue = deque([(root, 0)])      # [(node, column),]

        while queue:
            node, column = queue.popleft()
            if node:              #   HINT!!!
                column_table[column].append(node.val)

                queue.append((node.left, column-1))
                queue.append((node.right, column+1))
        return [column_table[i] for i in sorted(column_table.keys())]
        # Time = O(NlogN), Space = O(N)

        # BFS without sorting ==========================================
        if not root:
            return []

        column_table = defaultdict(list)
        queue = deque([(root, 0)])  # (node, column)
        min_col = max_col = 0

        while queue:
            node, column = queue.popleft()
            if node:
                column_table[column].append(node.val)
                min_col = min(min_col, column)
                max_col = max(max_col, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [column_table[i] for i in range(min_col, max_col + 1)]
        # Time = O(N), Space = O(N)

        # DFS ==========================================================
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x: x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret