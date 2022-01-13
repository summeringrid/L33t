class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:  # target is on the right side
                l = mid + 1
            elif nums[mid] > target:  # target is on the left side
                r = mid - 1
            else:  # nums[mid] == target
                return mid
        return -1

    # Time = O(logn)
    # Space = O(1)