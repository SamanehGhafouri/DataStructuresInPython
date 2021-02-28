# ***************************************** List comprehension ***********************
x = list()
y = ['a', 25, 'dog', 8.43]
tuplel = (10, 2)
z = list(tuplel)


# List comprehension
a = [m for m in range(8)]
print(a)

b = [i**2 for i in range(10) if i > 4]
print(b)
# ***************************************** DELETE ***********************

x = [5, 3, 8, 6]
del(x[1])
print(x)
del(x)

# ***************************************** Append ***********************

x = [5, 3, 8, 6]
x.append(7)
print(x)

# ***************************************** Extend ***********************

x = [5, 3, 8, 6]
y = [12, 13]
x.extend(y)
print(x)

# ***************************************** Insert ***********************

x = [5, 3, 8, 6]
x.insert(1, 7)                  # insert(index, value)
print(x)
x.insert(1, ['a', 'm'])
print(x)

# ***************************************** Pop *********************************

x = [5, 3, 8, 6]
x.pop()
print(x)
print(x.pop())

# ***************************************** Remove *********************************
x = [5, 3, 8, 6, 3]
x.remove(3)      # python starts finding the elements from the beginning of the list
print(x)         # finds the first matching

# ***************************************** Reverse *********************************

x = [5, 3, 8, 6]
x.reverse()
print(x)

# ***************************************** Sort *********************************

x = [5, 3, 8, 6]          # sorted() is not the inplace sort, it returns a new list
x.sort()                  # sort() is an inplace sort
print(x)

# ***************************************** inplace reverse *********************************

x = [5, 3, 8, 6]
x.sort(reverse=True)
print(x)