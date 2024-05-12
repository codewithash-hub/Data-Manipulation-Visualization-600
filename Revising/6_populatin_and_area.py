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
print(provinces)

print(provinces.index)
print(provinces.columns)
print(provinces.values)

