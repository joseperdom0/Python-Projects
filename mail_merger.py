# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

list_of_names = []

with open("./Input/Names/invited_names.txt") as names:
    for line in names:
        line.strip()
        list_of_names.append(line.strip())

print(list_of_names)

for name in list_of_names:
    with open("./Input/Letters/starting_letter.txt") as file:
        f = open(f"./Output/ReadyToSend/{name}.txt", "a")
        for line in file.readlines():
            replaced_line = line.replace("[name]", name)
            f.write(replaced_line)
            print(replaced_line)
        f.close()


