import pandas as pd
import numpy as np

data = pd.read_csv('healthexp.csv')
print(data.head())

nan = data.isnull().sum()
print("\n", nan)