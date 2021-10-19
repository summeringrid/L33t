"""
Dijkstra's algorithm

Algorithm for finding the shortest paths between nodes in a graph
DS: PriorityQueue: get the smallest value with O(log n) Time complexity
    Syntax: -> pq = PriorityQueue
            -> pq.put((0, start_vertex))
            -> while not pq.empty():
            -> (dist, curr_vertex) = pq.get()

Time = O(|E|+|V|log|V|) or  O(ElogV)
Space = O

Other notes:
 -> Achieve Dijkstra's algo through greedy.
 -> Dijkstra’s algorithm is very similar to Prim’s algorithm for minimum spanning tree.

Reference:
 -> https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
 -> https://stackabuse.com/dijkstras-algorithm-in-python/
"""


from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        # self.edges[u][v] = weight
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

        """
        print([[-1 for i in range(3)] for j in range(2)])
        # [[-1, -1, -1], [-1, -1, -1]]
        """

    def add_edge(self, u, v, t):
        self.edges[u][v] = t

    def dijkstra(self, start_vertex):
        D = {v: float('inf') for v in range(self.v)}
        # D = {0: inf, 1: inf, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf, 7: inf, 8: inf}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D



g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)

D = g.dijkstra(0)

# for vertex in range(len(D)):
#     print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])


# play around with PriorityQueue
test = PriorityQueue()
test.put(3)
test.put(6)
test.put(1)
test.put(0)
test.put(-3)
print(test)
print(test.get())
print(test.get())
print(test.get())
print(test.get())
print(test.get())
print(test.empty())

test2 = PriorityQueue(2)
test2.put((6, 1))
test2.put((3, 4))
print(test2)
print('maxsize =', test2.maxsize)
print(test2.get())
print(test2.empty())
print(test2.full())
test2.put((7, 4))
print(test2.full())
print(test2.get())
print(test2.get())

