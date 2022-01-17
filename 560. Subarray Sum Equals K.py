class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #         count = 0
        #         for start in range(0, len(nums)):
        #             sum = 0
        #             for end in range(start, len(nums)):
        #                 sum += nums[end]

        #                 if sum == k:
        #                     count += 1
        #         return count

        #     # Time = O(n^2)

        d = {}  # store the cumulative sum up to all the indices possible along with the number of times the same sum occurs.
        # mapping sum[i] --> no.of occurrences of sum
        d[0] = 1  # sum== 0 occurence 1
        count, sum = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum - k) in d:
                count += d[sum - k]
            d[sum] = d.get(sum, 0) + 1
        return count

        # [1,2,3,4,5,4,3, 2,1]
        # 9

        # 2,3,4
        # 4,5
        # 5,4
        # 4,3,2

        # times a subarray with sum k has occurred up to the current index
        # d = {0: 1, 1: 1, 3: 1, 6: 2, 10: 2, 13:1, 15: 1, }
        # sum = 25

