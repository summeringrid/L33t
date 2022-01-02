"""
https://www.lintcode.com/problem/1565/
"""


from collections import deque


class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """

    def modernLudo(self, length, connections):
        # Write your code here
        graph = self.build_graph(length, connections)
        queue = deque([1])
        distance = {1:0}
        while queue:
            curr_node = queue.popleft()
            right_limit = min(curr_node + 7, length + 1)        # because it is exclusive, so not +6 but +7
            for neighbor in range(curr_node + 1, right_limit):
                connected_nodes = self.get_unvisited_nodes(graph, distance, neighbor)
                for connected_node in connected_nodes:
                    if connected_node == length:        # reach the dest
                        return distance[curr_node] + 1
                    distance[connected_node] = distance[curr_node] + 1
                    queue.append(connected_node)
        return distance[length]

    def build_graph(self, length, connections):
        graph = {
                i : set()
                for i in range(1, length + 1)
        }
        for from_node, to_node in connections:
            graph[from_node].add(to_node)
        return graph

    def get_unvisited_nodes(self, graph, distance, node):
        unvisited_nodes = set()
        queue = deque([node])
        while queue:
            curr_node = queue.popleft()
            # if curr_node in distance, means it is already visited
            if curr_node in distance:
                continue
            unvisited_nodes.add(curr_node)
            for neighbor in graph[curr_node]:
                if neighbor not in distance:
                    queue.append(neighbor)
                    unvisited_nodes.add(neighbor)
        return unvisited_nodes





