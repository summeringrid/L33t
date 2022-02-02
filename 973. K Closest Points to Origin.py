class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Approach I: Time = O(NlogN), Space = O(N) =========================================

        points.sort(key=self.squared_distance)
        #  == points.sort(key=lambda x : self.squared_distance(x))
        return points[:k]

        # heapq: max heap --> negate the squared_distance value and return the first k element
        # Approach II: Time = O(N*log k), space = O(N + k) ===================================
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            cur_squared_dis = - self.squared_distance(points[i])
            if cur_squared_dis > heap[0][0]:  # current is negated val, so we need to keep the greater one
                heapq.heappushpop(heap, (cur_squared_dis, i))

        return [points[i] for (_, i) in heap]

def squared_distance(self, point):
    return point[0] ** 2 + point[1] ** 2
