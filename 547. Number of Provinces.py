class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # dfs

        if not isConnected:
            return 0

        n = len(isConnected)
        visited = [False] * n
        province = 0

        # adjList = {i:[] for i in range(n)}
        adjList = collections.defaultdict(list)

        # for c1, c2 in isConnected:
        #     adjList[c1].append(c2)
        #     adjList[c2].append(c1)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)

        def dfs(city):
            for nei in adjList[city]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                province += 1
                visited[i] = True
                dfs(i)
        return province

    # Time = O(n^2), Space = (n)