class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # brutal froce
        nums.sort()
        nums.reverse()
        return nums[k - 1]

        # Time = O(NlogN), N = len(nums)

        # Heap
        heapq.heapify(nums)  # can delete this line
        return heapq.nlargest(k, nums)[-1]