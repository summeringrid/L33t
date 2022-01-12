class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs[0] -> "eat"  ['e', 'a', 't']
        # strs[1] -> "tea"

        # for word in strs -> for char in word ->
        ans = collections.defaultdict(list)

        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

        # Time = O(n* klogk), n = len(strs), k = max(str in strs)
        # Space = O(n*m)

        # ---> optimize
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

        # Time = O(n*k), n=len(str), k=len(str)
        # Space = O(n*k)