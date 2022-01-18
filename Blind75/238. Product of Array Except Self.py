class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1
        # for num in nums:
        #     product *= num

        # output = []
        # for num in nums:
        #     if num == 0:
        #         output.append(0)
        #     else:
        #         output.append(int(product/num))

        # return output

        # can't use the above solution, controdiction:
        # input = [1,0,1,1,1,1,1,1,-1,1,1]
        # output = [0,-1,0,0,0,0,0,0,0,0,0]

        n = len(nums)
        ans = [0] * n
        ans[0] = 1

        # product on the left
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        R = 1
        for i in reversed(range(len(nums))):
            ans[i] *= R
            R *= nums[i]
        return ans

    # Time = O(n), Space = O(1)