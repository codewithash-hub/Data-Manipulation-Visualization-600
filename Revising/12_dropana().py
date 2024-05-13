import pandas as pd
import numpy as np

data = pd.DataFrame([
    [1, np.nan, 2],
    [2, 3, 5],
    [np.nan, 4, 6]
])

print(data.dropna(axis='columns'))