class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        # Time = O(E+V), Space = O(E+V)

        visited = set()
        res = 0

        adjList = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res


        # Union Find
        # Time = O(E*a(n)). Space = O(V)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):  # n1 is a node
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

