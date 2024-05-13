import pandas as pd

data = pd.Series([3, 5, 1, 6, 1], index=list('abcde'))

# loc attribute allows ibdexing and slicing that always references the explicit index.
print("loc method")
print(data.loc['a'])
print(data.loc['b': 'd'])

# iloc attribute allows indexing and slicing that always references the implicit python-style index.
print("iloc method")
print(data.iloc[1])
print(data.iloc[2:6])