class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Method 1: sorting and check if expected num in the sorted array
        # Time = O(nlogn) # Space = O(n) or O(1) if in place allowed
        nums.sort()
        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num


        # Method 2: use a set to store nums and traverse num in range of len(nums)+1 in set or not
        # Time = O(n) (created set: O(n); loop the range: O(n); each set insertion O(1))
        # Space = O(n)
        nums_set = set(nums)
        n = len(nums) + 1
        for num in range(n):
            if num not in nums_set:
                return num


        Time = O(n), Space = O(1)


        