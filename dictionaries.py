# ************************** Constructors
# Key/Value pairs
# Associative array, like Java HashMap
# Dicts are Unordered

x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(x)

x = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 55.9)])
print(x)

x = dict(pork=25.3, beef=33.8, chicken=22.7)
print(x)

# ************************** Dictionary Operations

x['shrimp'] = 38.2      # add or update
print(x)

del(x['shrimp'])        # delete an item
print(x)

print(len(x))           # get length of dict x

x.clear()               # delete all items from dict x
print(x)

del(x)                  # delete dict x

# ************************** Accessing keys and values in a dict

y = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(y.keys())
print(y.values())
print(y.items())

print('beef' in y)
print('clams' in y.values())

# ************************** Iterating a dict

for key in y:
    print(key, y[key])

for key, value in y.items():
    print(key, value)

