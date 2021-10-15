# Backtracking - recursion
# breadcrumb our path (i.e. mark the nodes we visited)

# from collections import defualtdict
# courseDict = defaultdict(list)


# Postorder DFS


# Topological
class GNode(object):
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []


class Solution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict, deque
        # key   : index of the node;
        # value : GNode
        graph = defaultdict(GNode)

        totalDeps = 0
        for relations in prerequisites:
            nextCourse, prevCourse = relations[0], relations[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1

        # start with the course without prerequesites
        noPrevCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                noPrevCourses.append(index)

        removedEdges = 0
        while noPrevCourses:
            course = noPrevCourses.pop()

            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1

                if graph[nextCourse].inDegrees == 0:
                    noPrevCourses.append(nextCourse)

        if removedEdges == totalDeps:
            return True
        else:
            # there's still some edge(s) left - > circle exits -> dead-lock (dependencies)
            return False


# DFS - neet code
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            # visitedSet = all courses along the curr DFS path
        visitedSet = set()

        def dfs(crs):
            if crs in visitedSet:
                return False
            if preMap[crs] == []:
                return True

            visitedSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # 【finish visiting it!!】for avoiding checking it again!!
            visitedSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        # Time = O(n), n is the course num; Space = O(n) for the hashmap

# preMap

# crs     pre
# 0       [1,2]
# 1       [3,4]
# 2       []
# 3       [4]
# 4       []


# start taking the course without any prerequisite
# if there is a circle, there may be impossible to take all courses


# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print("Dictionary:")
# print(Dict)
# print(Dict[1])


# from collections import defaultdict

# # Function to return a default
# # values for keys that is not
# # present
# def def_value():
#     return "Not Present"

# # Defining the dict
# d = defaultdict(def_value)
# d["a"] = 1
# d["b"] = 2

# print(d["a"])
# print(d["b"])
# print(d["c"])