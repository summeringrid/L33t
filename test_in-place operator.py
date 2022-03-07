a = set('abc')
a &= set('cbe')

print("a:", a)        # set(['c', 'b']), print result: {'c', 'b'}


# equal operation:
b = set('abc')
b.__iand__(set('cbe'))
print("b:", b)        # set(['c', 'b']), print result: {'c', 'b'}

"""
The less commonly used immutable frozenset object would be replaced in memory on the inplace update, 
and the variable name would point to the new object in memory.
"""
c = frozenset('abc')
c &= set('bce')
print("c:", c)


"""
Under the hood it does bit-wise binary operation.
i.e. 5 in binary is 0101 and 3 in binary is 0011
5 --> 0101
3 --> 0011
& --> 0001  "And" operation: both 1s the result is 1, 0 otherwise;
"""

x = 5
while x != 0:
    x &= x-1
    print(x)

# Application - LeetCode #338. Counting Bits


def countBits(n: int):
    ans = [0] * (n + 1)
    print('ans[{}] = {}'.format(0, ans[0]))
    for x in range(1, n + 1):
        ans[x] = ans[x & (x - 1)] + 1
        print('ans[{}] = {}'.format(x, ans[x]))
    return ans


print('result:', countBits(5))
