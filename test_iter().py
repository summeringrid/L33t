# Python3 code to demonstrate
# working of iter()

# initializing list
lis1 = [1, 2, 3, 4, 5]
print('lis1:', lis1)

# printing type
print("The list is of type : " + str(type(lis1)))

# converting list using iter()
lis1 = iter(lis1)

# printing type
print("The iterator is of type : " + str(type(lis1)))

# using next() to print iterator values
print(next(lis1))
print(next(lis1))
print(next(lis1))
print(next(lis1))
print(next(lis1))
