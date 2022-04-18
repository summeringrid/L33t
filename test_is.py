"""
The is keyword is used to test if two variables refer to the same object.

"""

x = ["apple", "banana", "cherry"]
y = x
print(x is y)

x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y)