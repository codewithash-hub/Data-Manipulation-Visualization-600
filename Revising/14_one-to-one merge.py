import pandas as pd

data1 = {
    'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
    'group': ['Accounting', 'Enginnering', 'Engineering', 'HR']
}

data2 = {
    'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
    'hire_date': [2004, 2008, 2012, 2014]
}

data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)

data3 = pd.merge(data1, data2)

print(data3)

print(data3.loc[data3.hire_date >= 2010])