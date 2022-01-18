class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]  # max(None, 0)

        for num in nums:
            if currSum < 0:
                currSum = 0

            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum

        ##################################

        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

        # Time = O(n), Space = O(1)