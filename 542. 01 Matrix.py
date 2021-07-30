class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Time = O(n), Space = O(n)
        rows = len(mat)
        cols = len(mat[0])
        inf = 10**10
        distance = [[inf] * cols for _ in range(rows)]
        
        queue = collections.deque()
        
        # def enqueue(r, c, d):
        #     distance[r][c] = d
        #     queue.append((r, c, d))
        
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    distance[r][c] = 0
                    queue.append((r, c, 0))
                    # enqueue(r, c, 0)
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while len(queue) > 0:
            r, c, d = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and distance[nr][nc] == inf:
                    queue.append((nr, nc, d + 1))
                    distance[nr][nc] = d + 1
                    # enqueue(nr, nc, d + 1)

        return distance
