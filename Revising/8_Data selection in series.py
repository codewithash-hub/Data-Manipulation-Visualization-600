import pandas as pd

data = pd.Series([3, 5, 1, 6, 1], index=list('abcde'))

print(data)
print("Is a in data? ", 'a' in data)
print(list(data.items()))
print()

# slicing by explicit index
print(data['a': 'c'])

# slicing by impicit integer index
print(data[0:2])

# masking
print(data[(data >= 2) & (data <= 5)])

# fancy indexing
print(data[['c', 'a']])