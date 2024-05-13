import pandas as pd

data1 = pd.DataFrame({
    'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
    'group': ['Accounting', 'Enginnering', 'Engineering', 'HR']
})



data2 = pd.DataFrame({
    'group': ["Accounting", 'Accounting','Engineering', "Engineering", 'HR', "HR"],
    'skills': ['Math', 'Spreadsheet', 'Software', 'Math', 'spreadsheet', 'Organization']
})

data_merge = pd.merge(data1, data2)
print(data_merge)
