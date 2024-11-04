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

country1 = 'Ukraine'
country2 = 'Uzbekistan'

if country1 in data and country2 in data:
    plt.figure(figsize=(15, 6))
    plt.plot(data[country1]['year'], data[country1]['gdp'], label=country1, marker='o')
    plt.plot(data[country2]['year'], data[country2]['gdp'], label=country2, marker='o')
    plt.xlabel('Рік')
    plt.ylabel('ВВП (дол. США)')
    plt.title(f'Динаміка ВВП: {country1} та {country2}')
    plt.legend()
    plt.grid()
    plt.xticks(data[country1]['year'])  
    plt.show()

plt.figure(figsize=(15, 6))

years = np.array(data[country1]['year']) 
gdp1 = np.array(data[country1]['gdp'])  
gdp2 = np.array(data[country2]['gdp'])  

width = 0.4  
x = np.arange(len(years)) 

plt.bar(x - width/2, gdp1, width, label=country1, color='skyblue')
plt.bar(x + width/2, gdp2, width, label=country2, color='orange')

plt.xlabel('Рік')
plt.ylabel('ВВП (дол. США)')
plt.title(f'Стовпчаста діаграма ВВП для {country1} та {country2}')
plt.xticks(x, years)
plt.legend()
plt.grid(axis='y')
plt.show()
