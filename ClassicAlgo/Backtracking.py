"""
All those who need to exhaust all the results should think of using backtracking


TEMPLATE:

"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def backtrack(remain, path, start):
            if remain < 0:
                return  # backtracking
            if remain == 0:
                res.append(path)        # res.append(list(path))  --> deep copy of the current combination
                return
            for i in range(start, len(candidates)):
                backtrack(remain - candidates[i], path + [candidates[i]], i)
                # path.pop()            # backtrack, remove the number from the combination

        backtrack(target, [], 0)
        return res


# Time = O(N**(T/M + 1))
# Space = O(N**(T/M))

# N = len(candidates), T = target val,  M = min(candidates) (the minimal value among the candidates)

"""
PRACTICE:
39. Combination Sum: https://leetcode.com/problems/combination-sum/


"""