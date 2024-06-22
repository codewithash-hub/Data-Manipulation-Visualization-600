import pandas as pd

data = pd.Series([3, 5, 1, 6, 1], index=list('abcde'))

print(data)
print("Is a in data? ", 'a' in data)
print(list(data.items()))
print()

data.loc['e'] = data.loc['e'] = 4
print("New Series:\n", data)

# slicing by explicit index
print('slicing by explicit index')
print(data.loc['a': 'c'])

# slicing by impicit integer index
print('slicing by impicit integer index')
print(data.iloc[0:3])

# masking
print('masking')
print(data.loc[(data >= 2) & (data <= 5)])

# fancy indexing
print('fancy indexing')
print(data.loc[['c', 'a']])