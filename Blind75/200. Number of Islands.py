class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # Time = O(M*N), M is rows and N is cols
        # Space = O(M*N)

        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(grid, r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return

            else:
                grid[r][c] = '-1'
                dfs(grid, r, c + 1)
                dfs(grid, r, c - 1)
                dfs(grid, r + 1, c)
                dfs(grid, r - 1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    islands += 1
        return islands
        # Note: check the grid value: String type; check out of boundary before checking the val

        # BFS
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    islands += 1
        return islands

    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = '0'
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y):
                    continue
                queue.append((next_x, next_y))
                grid[next_x][next_y] = '0'

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == '1'


        # Union Find
