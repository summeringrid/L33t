class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # brutal force
        # hashmap: num : count --> return :k
        dic = {}
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)

        # sort dic by its value
        sorted_dic = sorted(dic.items(), key=lambda item:item[1], reverse=True)

        res = []
        i = 0
        while i < k:
            res.append(sorted_dic[i][0])
            i += 1

        return res
        # Time = O(N + NlogN), Space = O(N)

        # optimal solution - > Time = O(N)
        # bucket sorting 0 - > len(nums)
        freq = [[] for i in range(len(nums) + 1)]  # index is freq 0~N: [num_list]
        dic = {}  # count
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)

        for n, c in dic.items():
            freq[c].append(n)

        res = []

        for i in range(len(nums), -1, -1):  # HINT: len(freq) doesn't work
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        # Time = O(N), Space = O(n)
        # (worst case: O(N + len(nums)*k))