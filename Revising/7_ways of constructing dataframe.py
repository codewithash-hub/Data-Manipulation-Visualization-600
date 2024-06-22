import pandas as pd
import numpy as np

# from a single Series object 

population = {
    "Limpopo": 282121,
    "Gauteng": 3198283,
    "Kwazulu-Natal": 129412,
    "Eastern Cape": 1293084,
    "Northern Cape": 93233
}

area_dictionary = {
    "Limpopo": 1435,
    "Gauteng": 453,
    "Kwazulu-Natal": 2436,
    "Eastern Cape": 6743,
    "Northern Cape": 10662
}

ser = pd.Series(population)

print('From a single series object')
pop = pd.DataFrame(ser, columns = ['Population'])
print(pop)

# From a list of dictionaries
print('From a list of dictionaries')
data = [{'a': i, 'b': i * 2} for i in range(3)]
df = pd.DataFrame(data)
print(df)

# From a dicts of series object
area = pd.Series(area_dictionary)
print('From a dicts of series object')
provinces = pd.DataFrame({'Population': ser, "Area": area})
print(provinces)

# From 2D Numpy Array
print('From 2D Numpy Array')
array = np.random.rand(3, 2)
df2 = pd.DataFrame(array, columns=['foo', 'bar'], index=list('abc'))
print(df2)

# From a Numpy structured array
print('From a Numpy structured array')
A = np.ones(3, dtype=[('A', 'i8'), ('B', 'f8')])
print("ones: ", A)
a = pd.DataFrame(A)
print(a)