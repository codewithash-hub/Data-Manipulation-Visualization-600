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

df4 = pd.DataFrame({
    'group': ['Accounting', 'Engineering', 'HR'],
    'supervisor': ['Carly', 'Guido', 'Steve']
})

data4 = pd.merge(data3, df4)
print(data4)