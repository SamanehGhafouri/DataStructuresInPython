# ************************** Constructors
# Store non-duplicate items
# Very fast access vs lists
# Math Set ops(union, intersect)
# Sets are Unordered can't be sorted

# Creating new sets
x = {3, 5, 3, 5}
print(x)

y = set()
print(y)

# *************************** Set Operations

x = {3, 8, 5}
print(x)
x.add(7)
print(x)

x.remove(3)
print(x)

print(len(x))

print(5 in x)

print(x.pop(), x)       # pop random item from set x

x.clear()
print(x)

# *************************** Mathematical set operations

# Intersection (AND): set1 & set2
# Union (OR): set1|set2
# Symmetric difference (XOR): set1 ^ set2
# difference (in set1 but not set2): set1 - set2
# Subset(set2 contains set1): set1 <= set2
# Subset(set1 contains set2): set1 >= set2

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)




