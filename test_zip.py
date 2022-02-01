strs = ["flower","flow","flight"]

print(zip(strs))
print(zip(*strs))

for i, c in enumerate(strs):
    print(i, c)


print('=========== zip(strs) ===========')
for i, c in enumerate(zip(strs)):
    print(i, c)

print('=========== zip(*strs) =========')
for i, c in enumerate(zip(*strs)):
    print(i, c)


print('min(strs),',min(strs))