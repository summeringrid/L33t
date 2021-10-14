# python syntax for creating a matrix
import numpy as np

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


# # approach I
# # can't print out the matrix
# for i in range(len(A)):
#     print("--")
#     for j in range(len(A[0])):
#         print(A[i][j])


# # Approach II
print('\n'.join([''.join(['{:3}'.format(item) for item in row])
      for row in A]))

# # Approach III
print(np.array(A))

# C = np.array([[1,2,3],[3,4,5],[7,8,9]])
# print(C)


B = [[None] * 3]*4

# for i in range(len(B)):
#     print("--")
#     for j in range(len(B[0])):
#         print(B[i][j])
# print(B)

print(np.array(B))
print()