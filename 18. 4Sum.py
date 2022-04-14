class Solution:
    # convert 4sum into 3sum, in 3sum helper function, degrade the prob into 2sum
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                threeSum = self.threeSum(nums[i + 1:], target - nums[i])
                for item in threeSum:
                    res.append([nums[i]] + item)  # opertion between 2 lists
        return res

    def threeSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i - 1]:
                while l < r:
                    s = nums[l] + nums[r]
                    if s < t:
                        l += 1
                    elif s > t:
                        r -= 1
                    else:  # s == t
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]: l += 1
                        while l < r and nums[r] == nums[r - 1]: r -= 1
                        l += 1
                        r -= 1
        return res

    # Time = O(n^2) Space = O(n)