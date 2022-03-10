# file = open("weather_data.csv","r")
# data = file.readlines()
# print(data)
# file.close()

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    next(data)
    for row in data:
        temperatures.append(int(row[1]))

print(temperatures)