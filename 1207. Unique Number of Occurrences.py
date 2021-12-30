class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        occur = dict()

        for num in arr:
            if num in occur:
                occur[num] += 1
            else:
                occur[num] = 1

        hashSet = set()

        for key in occur:
            hashSet.add(occur[key])

        return len(hashSet) == len(occur)


    # return len(set([arr.count(x) for x in set(arr)])) == len(set(arr))
    # ===

        arraySet = set(arr)
        arrayCount = set()
        for x in arraySet:
            arrayCount.add(arr.count(x))
        return len(arrayCount) == len(arraySet)
