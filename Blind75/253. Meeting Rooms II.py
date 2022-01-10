class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals or len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1

        intervals.sort()
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])  # min-heap: store the end time
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)

    # Time = O(nlogn)
    # Space = O(n), n = len(intervals)