class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1],
               [-1, 1], [1, 1], [-1, -1], [-1, 1]]

        queue = collections.deque([(0, 0, 1)])  # index & dist
        seen = set()

        while queue:
            r, c, dist = queue.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in seen and grid[nr][nc] == 0:
                        seen.add((nr, nc))
                        queue.append((nr, nc, dist + 1))

        return -1

        # Time = O(N) N = num(cells), Space = O(N)