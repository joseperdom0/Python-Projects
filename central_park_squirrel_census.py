import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

color_series_complete = data["Primary Fur Color"]

# dropping Null
color_series = color_series_complete.dropna()

#print(color_series)

counts = pandas.Series(color_series).value_counts()
number_of_black = counts.get('Black')
number_of_cinnamon = counts.get('Cinnamon')
number_of_gray = counts.get('Gray')

data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [number_of_gray, number_of_cinnamon, number_of_black]

}

data_counts = pandas.DataFrame(data_dictionary)
print(data_counts)
