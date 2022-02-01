import functools
arr = [1, 3, 5, 6, 2, ]

print(functools.reduce(lambda a, b: a+b, arr))
