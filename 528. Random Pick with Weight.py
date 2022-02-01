class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0

        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        # linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i

        # binary search to find the target zone
        low, high = 0, len(self.prefix_sums) - 1
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid  # HINT: shouldn't be mid - 1
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()