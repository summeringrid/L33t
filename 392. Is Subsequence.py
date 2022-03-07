class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

    # 2ptr, Time = O(|T|), Space = O(1)



# DP solution, Time = Space = O(|S| * |T|))

matrix = [[1] * 3 for _ in range(7)]
print(matrix)