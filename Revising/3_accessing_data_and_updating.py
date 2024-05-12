import pandas as pd

data = [3, 1, 5, 1, 2, 7]
indices = ['a', 'b', 'c', 'd', 'e', 'f']

srs = pd.Series(data=data, index=indices)

# ser.iloc[pos]

print(srs.iloc[1])
print(srs.iloc[1:3])
change = srs.iloc[4] = 100
print(change)
print(srs)