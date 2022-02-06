class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}  # mapping prefix sum module to its index
        summ = 0
        for i, n in enumerate(nums):
            summ = (summ + n) % k
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False

        # Time = O(N), N = len(num)
        # Space = O(N)