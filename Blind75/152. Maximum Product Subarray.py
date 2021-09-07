class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            temp = n * currMax
            currMax = max(n, n * currMax, n * currMin)
            currMin = min(n, temp, n * currMin)

            result = max(result, currMax, currMin)
        return result

    # T = O(N), M = O(1)