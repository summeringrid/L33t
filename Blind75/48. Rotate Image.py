import numpy as np

print("python syntax for creating a matrix")

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

########################################
print("approach I - nested for loop:")
########################################
# can't print out the matrix
for row in range(len(A)):
    for col in range(len(A[0])):
        print(A[row][col], ' ', end='')
    print('\n')
########################################
print("approach II - .join")
########################################
print([''.join(['{:1}'.format(item) for item in row])
      for row in A])

print('\n'.join(([''.join(['{:3}'.format(item) for item in row])
      for row in A])))


########################################
print("approach III - numpy")
########################################

C = np.array([[1,2,3],[3,4,5],[7,8,9]])
print(C)


B = [[None] * 3]*4

# for i in range(len(B)):
#     print("--")
#     for j in range(len(B[0])):
#         print(B[i][j])
# print(B)

print(np.array(B))
print("try nested loop")

D = [[1,2,3],[3,4,5],[7,8,9]]
for row in range(len(D)):
    for col in range(len(D[0])):
        print(D[row][col], ' ', end="")
    print('\n')
print('-----------')
for row in D:
    for item in row:
        print(item, ' ', end="")
    print('\n')




# 48 rotate image
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Approach I
        # Time =O(M), M is the number of cells in the matrix
        #         n = len(matrix)

        #         for i in range(n//2 + n%2):
        #             for j in range(n//2):
        #                 temp = matrix[n-1-j][i]
        #                 matrix[n-1-j][i] = matrix[n-1-i][n-j-1]
        #                 matrix[n-1-i][n-j-1] = matrix[j][n-1-i]
        #                 matrix[j][n-1-i] = matrix[i][j]
        #                 matrix[i][j] = temp

        # Approach II
        # Time = O(n), n is the cell num of the matrix; Space = O(1)
        #         self.transpose(matrix)
        #         self.reflect(matrix)

        #     def transpose(self, matrix):
        #         n = len(matrix)

        #         for i in range(n):
        #             for j in range(i, n):
        #                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #     def reflect(self, matrix):
        #         n = len(matrix)

        #         for i in range(n):
        #             for j in range(n//2):
        #                 matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

        # Approach III
        # Time = O(m) m is the cell num in the matrix (we can also say it is n^2, n is the len(matrix))
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1

