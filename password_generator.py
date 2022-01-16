# Password Generator Project
import random
# import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

mapping = [[letters], [numbers], [symbols]]
total_characters = nr_letters + nr_symbols + nr_numbers
password = ""

for _ in range(nr_letters):
    selected_character = random.choice(letters)
    password += selected_character

for _ in range(nr_numbers):
    selected_character = random.choice(numbers)
    password += selected_character
for _ in range(nr_symbols):
    selected_character = random.choice(symbols)
    password += selected_character

pass_list = list(password)
random.shuffle(pass_list)
shuffled_password = ''.join(pass_list)
print(shuffled_password)
# pyperclip.copy(shuffled_password)
# print("Generated password copied to clipboard.")
