class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # can't split one single weight, so the max(single weight) is the minum capacity
        # if k = 1, the max cap we need to considier is the sum(weights)
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            res, total = 1, 0
            for w in weights:
                if total + w > mid:
                    res += 1
                    total = w
                else:
                    total += w
                    # ==
                # if total + w > mid:
                #     res += 1
                #     total = 0
                # total += w
            if res <= days:  # on the minmum side
                hi = mid  # check narrow down in place, end up with lo = hi
            else:
                lo = mid + 1

        return hi  # either hi or lo  (but not mid)

    # Time = O(M * logN) , M = len(weights)
    # O(1)???