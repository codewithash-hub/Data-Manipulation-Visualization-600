import pandas as pd

data = [.25, .5, .7, 1.]
data = pd.Series(data, index = ['a', 'b', 'c', 'd'])

print(data)

print(data.iloc[1])
print()
print(data.iloc[1:3])