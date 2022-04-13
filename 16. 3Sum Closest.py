class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        final = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if curr == target:
                    return curr

                if abs(curr - target) < abs(final - target):
                    final = curr

                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
        return final

    # Time = O(n*n), Space = O(1)