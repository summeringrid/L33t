class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # Approach 1: brutal force
        nums.sort()
        nums.reverse()
        return nums[k - 1]

        # Neat code:
        nums.sort()
        return nums[len(nums) - k]

        # Time = O(NlogN), N = len(nums)

        # Approach 2: Heap
        # heapq.heapify(nums)  # can delete this line
        return heapq.nlargest(k, nums)[-1]

        # use maxHeap, no need to sort all the array
        # Time = k * logN

        # Approach 3: Quicksort
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, ptr = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]

            if ptr > k:     return quickSelect(l, ptr - 1)
            if ptr < k:
                return quickSelect(ptr + 1, r)
            else:
                return nums[ptr]

        return quickSelect(0, len(nums) - 1)

        # Time = O(n)
        # n + n/2 + n/4 + n/8 + ..... = 2n
