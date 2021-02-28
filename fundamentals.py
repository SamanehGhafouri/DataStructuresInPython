# *************************** Indexing ***************************

# String
x = 'frog'
print(x[3])

# List
x = ['pig', 'cow', 'horse']
print(x[1])

# Tuple
x = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(x[0])

# ************************** Slicing ********************************
# [start: end+1: step]

x = 'computer'
print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])


# ************************** Adding/ Concatenating *******************

# String
x = 'horse' + 'shoe'
print(x)

# List
y = ['pig', 'cow'] + ['horse']
print(y)

# Tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig') + ('Lucci',)  # Note: if you wanna add to tuple in the pranticis you need
print(z)                                                # to add comma ('Lucci',) for the tuple to realize
                                                        # that we are adding a tuple

# ****************************** Multiplying ***************************

# String
x = 'bug' * 3
print(x)

# List
y = [8, 5] * 3
print(y)

# tuple
z = (2, 4) * 3
print(z)

# **************************** Checking membership **********************

x = 'bug'
print('u' in x)

y = ['pig', 'cow', 'horse']
print('cow' not in y)

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print('Niklas' in z)

# ****************************** Iterating *******************************

x = [7, 8, 3]
for item in x:
    print(item)

y = [7, 8, 3]
for index, item in enumerate(y):
    print(index, item)

# ****************************** Number of items *************************

x = 'bug'
print(len(x))

y = ['pig', 'cow', 'horse']
print(len(y))

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(len(z))

# ******************************* Find Minimum ***************************

x = 'bug'
print(min(x))

y = ['pig', 'cow', 'horse']
print(min(y))

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(min(z))

# ******************************** Find Maximum **************************

x = 'bug'
print(max(x))

y = ['pig', 'cow', 'horse']
print(max(y))

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(max(z))

# ********************************* Find the Sum of items ****************

y = [2, 5, 8, 12]
print(sum(y[-2:]))

z = (50, 4, 7, 19)
print(sum(z))

# *********************************** Sorting *****************************

x = 'bug'
print(sorted(x))

y = ['pig', 'cow', 'horse']
print(sorted(y))

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(z))

# sort based on the second letter
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(z, key=lambda k:k[1]))

# *********************************** Count *****************************

x = 'hippo'
print(x.count('p'))

y = ['pig', 'cow', 'horse', 'cow']
print(y.count('cow'))

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z.count('Kevin'))

# *********************************** Index of an item *********************

x = 'hippo'
print(x.index('p'))

y = ['pig', 'cow', 'horse', 'cow']
print(y.index('cow'))

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z.index('Kevin'))

# *********************************** Unpacking items in a sequence *********

x = ['pig', 'cow', 'horse']
a, b, c = x
print(a, b, c)