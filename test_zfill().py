"""
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done.

"""

a = '1'
b = '9'
n = max(len(a), len(b))
a, b = a.zfill(n), b.zfill(n)

# print(n)            # 1
# print(a)            # 1
# print(b)            # 9

# Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print('x:', x)


a = "hello"
b = "welcome to the jungle"
c = "10.000"

print('a:', a.zfill(10))
print('b:', b.zfill(10))
print('c:', c.zfill(10))
