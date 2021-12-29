class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # Approach 1: brutal force
        nums.sort()
        nums.reverse()
        return nums[k - 1]

        # Time = O(NlogN), N = len(nums)

        # Approach 2: Heap
        # heapq.heapify(nums)  # can delete this line
        return heapq.nlargest(k, nums)[-1]

        # use maxHeap, no need to sort all the array
        # Time = k * logN

        # Approach 3: Quicksort


        # Time = O(n)
        # n + n/2 + n/4 + n/8 + ..... = 2n
