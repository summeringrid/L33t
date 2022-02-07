class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}  # mapping (r + c) to the cell val
        for r in range(len(mat)):
            for c in range(len(mat[r])):  # HINT: going diagonal!!
                if r + c not in d:
                    d[r + c] = [mat[r][c]]  # HINT: initialize the value as a list
                else:
                    d[r + c].append(mat[r][c])

        res = []
        for i, arr in d.items():
            if i % 2 == 0:
                # res.append(arr[::-1])         # HINT This doesn't work!!
                [res.append(n) for n in arr[::-1]]
            else:
                [res.append(n) for n in arr]
        return res

#      # Time = O(M*N), M = rows, N =  cols
#      # Soace = O(M*N)

