class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = dict()

        for num in arr:
            if num in occur:
                occur[num] += 1
            else:
                occur[num] = 1

        hashSet = set()

        #         for val in occur.values:
        #             hashSet.add(val)
        for key in occur:
            hashSet.add(occur[key])

        return len(hashSet) == len(occur)

    # return len(set([arr.count(x) for x in set(arr)])) == len(set(arr))