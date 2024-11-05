import csv
import matplotlib.pyplot as plt
import numpy as np

filename = 'lab14task2.csv'
data = {}

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if len(row) < 5:
            continue
        country = row[0].strip()
        year_str = row[2].strip()
        gdp_str = row[4].strip()

        if year_str.isdigit() and gdp_str:
            year = int(year_str)
            gdp = float(gdp_str)

            if country not in data:
                data[country] = {'year': [], 'gdp': []}
            data[country]['year'].append(year)
            data[country]['gdp'].append(gdp)

country = input("Enter the country to display: ")

if country in data:
 
    plt.figure(figsize=(15, 6))
    plt.plot(data[country]['year'], data[country]['gdp'], label=country, marker='o')
    plt.xlabel('Рік')
    plt.ylabel('ВВП (дол. США)')
    plt.title(f'Динаміка ВВП: {country}')
    plt.legend()
    plt.grid()
    plt.xticks(data[country]['year'])
    plt.show()

    plt.figure(figsize=(15, 6))

    years = np.array(data[country]['year'])
    gdp = np.array(data[country]['gdp'])

    plt.bar(years, gdp, color='skyblue', label=country)
    plt.xlabel('Рік')
    plt.ylabel('ВВП (дол. США)')
    plt.title(f'Стовпчаста діаграма ВВП для {country}')
    plt.xticks(years)
    plt.legend()
    plt.grid(axis='y')
    plt.show()
else:
    print("The country is not found in the data.")