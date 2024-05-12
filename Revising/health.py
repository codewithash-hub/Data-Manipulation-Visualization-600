import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("healthexp.csv")


print(data.head())
print()

year = pd.Series(data['Year'])
print(year)

# plt.plot(year, color = 'b')
# plt.show()

print(year.values)
print(year.index)