class Solution:
    def jump(self, nums: List[int]) -> int:
        # # Approach I
        # jump = 0
        # l = r = 0
        # while r < len(nums)-1:
        #     jump += 1
        #     furthest = max(i + nums[i] for i in range(l, r+1))
        #     l, r = r+1, furthest
        #
        # return jump

        if len(nums) <= 1: return 0
        jump = 1
        l, r = 0, nums[0]
        while r < len(nums) - 1:
            jump += 1
            furthest = max(i + nums[i] for i in range(l, r + 1))
            l, r = r + 1, furthest

        return jump

    # Time = O(n), Space = O(1)