import pandas as pd

# data can a scalar, which is repeated to fill the specified index.

data = pd.Series(9, index=[100, 200, 300])
print(data)

# Or it can be a dictionary, index defaults to the dictionary key.

ser = pd.Series({2: 'a', 5:'b', 8:'c'})
print(ser)

# The index can be set to control the order or the subset of keys used.
ser2 = pd.Series({2: 'a', 5:'b', 8:'c'}, [5, 2])
print(ser2)
