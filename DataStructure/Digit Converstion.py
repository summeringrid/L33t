# convert str into int without using built-in cast
digitStr = '1'
digitInt = ord(digitStr) - ord('0')     # digitInt = 1
# print(digitInt)

"""
ASCII TABLE: https://upload.wikimedia.org/wikipedia/commons/7/7b/Ascii_Table-nocolor.svg
Online Converter: https://onlinestringtools.com/convert-ascii-to-string
ord('a') == 97
ord('A') == 65

ord('0') == 48
ord('1') == 49

"""

str = '''Geeks
for
geeks'''
print("Display with ascii function : ", ascii(str))
print("Display with print function : ", str)
