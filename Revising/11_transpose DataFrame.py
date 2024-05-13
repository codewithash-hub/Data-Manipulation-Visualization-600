import pandas as pd

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

pop = pd.Series(population)
area = pd.Series(area_dictionary)

provinces = pd.DataFrame({'Population': pop, "Area": area})

provinces['Density'] = provinces['Population'] / provinces['Area']

#  transposing DataFrame
transpose = provinces.transpose()
print(transpose)

# in the loc indexer we can combine masking and fancy indexing.
print(transpose.loc['Density'] > 120, ['Population', 'Density'])

# Displaying values in the first 3 rows using iloc
print(transpose.iloc[:3, :2])


