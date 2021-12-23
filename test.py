a = '1'
b = '9'
n = max(len(a), len(b))
a, b = a.zfill(n), b.zfill(n)

# print(n)
# print(a)
# print(b)

txt = "50"
x = txt.zfill(10)
print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

print('===== Shift Operators')
print(2>>5)     # 0     # shift to left by 5 bits
print(2<<5)     # 64    # shift to right by 5 bits
print(1000>>2)  # 250
