# ************************** Constructors
# they are immutable (can't add/change) once it is created
# Useful for fixed data
# Faster than lists
# Sequence type

x = ()
x = (1, 2, 3)
x = 1, 2, 3
x = 2,  # comma tells python it is a tuple
print(x, type(x))

list1 = [2, 4, 6]
x = tuple(list1)
print(x, type(x))

# ************************** Tuples are immutable

x = (1, 2, 3)
# del(x[1])   # this will fail because immutable
# x[1 ] = 8   # this will fail
print(x)

y = ([1, 2], 3)
del(y[0][1])
print(y)

y += (4, )
print(y)