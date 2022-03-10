import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
'''
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
'''
print(data["temp"])
'''
0    12
1    14
2    15
3    14
4    21
5    22
6    24
'''

# data to dictionary
data_dict = data.to_dict()
print(data_dict)
"""{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
"""

temp_list = data["temp"].to_list()
print(temp_list)
'''[12, 14, 15, 14, 21, 22, 24]'''

average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)

print(data["temp"].mean())

# pandas behind the scenes creates attributes with the name of the columns
# for example:
print(data.condition)
'''0     Sunny
1      Rain
2      Rain
3    Cloudy
4     Sunny
5     Sunny
6     Sunny
Name: condition, dtype: object

'''
# printing by row
print(data[data.day == "Monday"])
'''0  Monday    12     Sunny'''
# day with highest temperature

print(data[data.temp == data.temp.max()])

# create a dataframe from scratch
data_from_dictionary = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 54, 6]

}
data_from_scratch = pandas.DataFrame(data_from_dictionary)
print(data_from_scratch)
'''0      Amy      76
1    James      54
2   Angela       6'''
# convert to csv file
data_from_scratch.to_csv("new_data.csv"
                         )