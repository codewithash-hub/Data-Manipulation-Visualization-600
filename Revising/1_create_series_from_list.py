import pandas as pd

data = [.25, .5, .7, 1.]
data = pd.Series(data, index = ['a', 'b', 'c', 'd'])

print(data)