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



nums1 = [1,2,3,4]
nums2 = [5,6,7,8]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)