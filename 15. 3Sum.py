class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

                # THINK: why this works as well? :)
                # else:
                #     res.append([nums[i], nums[l], nums[r]])
                #     l += 1
                #     while nums[l] == nums[l - 1] and l < r:
                #         l += 1

                # ANSWER: because we already guaranteed the nums[l] changes, then the combination will be unique

        return res
        
        # Time = O(n^2), Space = O(n)
