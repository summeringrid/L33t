class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]  # 0...N-1 --> 0...N

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        # Time = O(N), Space = O(n)
        # (worst case: O(N + len(nums)*k))