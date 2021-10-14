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




# 38
