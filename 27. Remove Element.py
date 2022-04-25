class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 2ptr, sliding window
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:       # after swapping, the updated nums[l] still can == val, so we need else statement
                l += 1
        return l

        # # 1 pointer
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            i += 1
        return i

    # Time = O(n), Space = O(1)
