s = 0
before = [[1,2],[3,4]]
after = [[],[]]
for i in range(2):
    for j in range(1):
        print('s', s)
        print('i=', i, 'j=', j, 'before=', before[i][j], '\n', end='')
        s += before[i][j]
print('\nres', s)

# print(after)
