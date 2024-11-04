import csv
import matplotlib.pyplot as plt
filename = 'lab14.csv'  
years = []
gdp_per_capita = []

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    for row in reader:
        if int(row[2]) :
            years.append(row[2])
            gdp_per_capita.append(float(row[4]))
plt.figure(figsize=(8, 8))
plt.pie(gdp_per_capita, labels=years, autopct='%1.1f%%', startangle=140)
plt.title('Частка ВВП на душу населення по роках')
plt.show()
