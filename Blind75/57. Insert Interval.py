class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]],
        # newInterval = [4,8]
        # Output: [[1,2],[3,10],[12,16]]

        # Approach I: simulate all process -- linear iteration (greedy)

        newStart, newEnd = newInterval
        idx, n = 0, len(intervals)
        res = []
        while idx < n and intervals[idx][0] < newStart:
            res.append(intervals[idx])
            idx += 1

        # Note: add newInterval: 1. no overlap; 2. overlap
        if not res or res[-1][1] < newStart:
            res.append(newInterval)
        else:  # res[-1][1] >= newStart
            res[-1][1] = max(res[-1][1], newEnd)

        # After adding the newInterval, deal with the following rest elements

        while idx < n:
            # 1. no overlap; 2. has overlap(s)

            interval = intervals[idx]
            start, end = interval
            idx += 1

            if res[-1][1] < start:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], end)
        return res

        # Time = O(n), Space =O(n)

        # Approach II Greedy

        output = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:  # deal with the overlap, use greedy to update the newInterval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        output.append(newInterval)

        return output