import random
import pandas
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {key: value for (key, value) in student_scores.items() if value > 59}
print(passed_students)

# Exercise 01
sentence = "What is the airspeed velocity of an Unladen Swallow"

count_words = {word: len(word) for word in sentence.split()}
print(count_words)

# exercise 02
# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)


# From pandas DataFrame

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row ) in student_data_frame.iterrows():
    print(row.score)
    # print(row)