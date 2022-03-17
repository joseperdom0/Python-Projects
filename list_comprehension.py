import pandas

numbers = [1, 2, 3, 4]
new_list = [n + 1 for n in numbers]
print(new_list)

new_range = [n * 2 for n in range(1, 5)]
print(new_range)

ex_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in ex_numbers]
print(squared_numbers)

even_numbers = [num for num in ex_numbers if num % 2 == 0]
print(even_numbers)

list_file1 = pandas.read_csv("file1.txt", sep= ' ', header= None)
list_1 = list_file1[0].to_list()

list_file2 = pandas.read_csv("file2.txt", sep= ' ', header= None)
list_2 = list_file2[0].to_list()
# print(list_1, list_2)

occurrence = [num for num in list_1 if num in list_2]
print(occurrence)