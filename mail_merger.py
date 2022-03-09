list_of_names = []

with open("./Input/Names/invited_names.txt") as names:
    for line in names:
        line.strip()
        list_of_names.append(line.strip())


for name in list_of_names:
    with open("./Input/Letters/starting_letter.txt") as file:
        f = open(f"./Output/ReadyToSend/{name}.txt", "a")
        for line in file.readlines():
            replaced_line = line.replace("[name]", name)
            f.write(replaced_line)
        f.close()


