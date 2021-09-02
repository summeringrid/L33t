class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        hashmap = {}
        for i in range(N):
            complement = target - nums[i]
            if complement in hashmap:  # not in the nums
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

        # Time = O(N)
        # Space = O(N)

        # Optimized
        # lib = {}
        # for i, n in enumerate(nums):
        #     if n in lib:
        #         return [lib[n], i]
        #     lib[target - n] = i