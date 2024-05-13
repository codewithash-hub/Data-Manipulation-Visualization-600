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

print("Area\n", provinces.Area)
print("Population\n", provinces.Population)

# adding a new column
provinces['Density'] = provinces['Population'] / provinces['Area']

print(f"Provinces with \"Density\" column\n {provinces}")