import itertools

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = iter(list1)

print(list1)
print(list2)

# cycle()
str1 = 'abc'
cycle1 = itertools.cycle(str1)
print(cycle1)

test2 = itertools.count(10)
print(test2)

iter = iter(list1)
# dropwhile =