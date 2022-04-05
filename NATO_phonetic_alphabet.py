import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(file)
# print(file)
# print(df)

nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_alphabet)

def nato():
    word = input("Please enter your word to decode: ").upper()
    decoded =  []
    # for char in word:
    #     for (key, value) in nato_alphabet.items():
    #         if char.title() == key:
    #             decoded.append(value)
    try:
        decoded = [nato_alphabet[char] for char in word]
    except KeyError:
        print("not found")
        nato()
    else:
        print(decoded)

nato()