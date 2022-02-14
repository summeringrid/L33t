class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        start = 1
        end = max(ribbons)
        # finding  length for the the target k pieces
        while (start <= end):
            mid = start + (end - start) // 2
            res = 0
            for i in ribbons:
                res += i // mid
            # exit larger length
            if res >= k:
                start = mid + 1
            else:
                end = mid - 1
        return end

        # Time = O(Nlog(M))), N = nums of ribbons, M =max(ribbons)




