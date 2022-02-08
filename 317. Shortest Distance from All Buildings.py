class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        distance = [[0 for _ in range(cols)] for _ in range(rows)]
        reach = [[0 for _ in range(cols)] for _ in range(rows)]

        buildingNum = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    buildingNum += 1
                    q = [(r, c, 0)]

                    isVisited = [[False for _ in range(cols)] for _ in range(rows)]

                    for y, x, d in q:
                        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                            nr = y + dy
                            nc = x + dx

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and not isVisited[nr][nc]:
                                distance[nr][nc] += d + 1
                                reach[nr][nc] += 1

                                isVisited[nr][nc] = True
                                q.append((nr, nc, d + 1))

        shortest = float("inf")
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    shortest = min(shortest, distance[i][j])

        if shortest < float("inf"):
            return shortest
        else:
            return -1

        # Time = O(M^2 * N^2)   <-- (M⋅N)/2⋅(M⋅N)/2
        # Space = O(N * M)
