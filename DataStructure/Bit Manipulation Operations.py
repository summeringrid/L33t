"""
convert str into int without using built-in cast

todo: Question - only can convert 0-9?
"""
print('===== str into int =====')
digitStr = '1'
# digitInt = ord(digitStr) - ord('0')
print("digitStr int value:", ord(digitStr))
# print("digitInt:", digitInt)

"""
ASCII TABLE: https://upload.wikimedia.org/wikipedia/commons/7/7b/Ascii_Table-nocolor.svg
Online Converter: https://onlinestringtools.com/convert-ascii-to-string
ord('a') == 97
ord('A') == 65

ord('0') == 48
ord('1') == 49

"""
print('===== ASCII str display =====')
str = '''Geeks
for
geeks'''
print("Display with ascii function : ", ascii(str))
print("Display with print function : ", str)


# num1 = '11'
# test1 = ord(num1) - ord('0')
# print(test1, type(test1))


"""
convert binary base number into decimal integer

decimal_num = int(binary_str, 2)
"""
print('===== binary into decimal =====')
a = "11"
b = "1"
decimal_a, decimal_b = int(a, 2), int(b, 2)
print(a,'convert to', decimal_a, '\n', b, 'convert to', decimal_b)

"""
convert binary base number into decimal integer

binary_num = bin(decimal_num)
"""
print('===== decimal into binary =====')
c = 3
d = 1
bin_c, bin_d= bin(c), bin(d)
print(c, 'into', bin_c)
print(d, 'into', bin_d)


