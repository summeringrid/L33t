"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

在图中从顶点A到顶点B有一条有向路径，则顶点A一定排在顶点B之前，满足这样的条件的顶点序列称为一个拓扑序。
拓扑排序有两个步骤：
1.从队列中获取一个入度为0的顶点
2.获取该顶点边，将边的另一端顶点入度减一，如果为0，也入队列
重复步骤1和2，直到队列为空，得到的出队顺序即为一个合理的拓扑序。


Time:
假设n个点，m条边；
记录拓扑序空间复杂度为O(n)，记录入度最坏复杂度为O(n)，空间复杂度O(n)；
记录每个点的入度为O(m)，拓扑排序为O(m)，时间复杂度O(m)。

"""


class BFS_Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        node_to_indegree = self.get_indegree(graph)

        # bfs
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1

        return node_to_indegree


class DFS_Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        indegree = {}
        for x in graph:
            indegree[x] = 0

        for i in graph:
            for j in i.neighbors:
                indegree[j] += 1

        ans = []
        for i in graph:
            if indegree[i] == 0:
                self.dfs(i, indegree, ans)
        return ans

    def dfs(self, i, indegree, ans):
        ans.append(i)
        indegree[i] -= 1
        for j in i.neighbors:
            indegree[j] -= 1
            if indegree[j] == 0:
                self.dfs(j, indegree, ans)