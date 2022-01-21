def encrypt(cypher_text, cypher_shift):
    message = []
    for letter in cypher_text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            shifted_letter = alphabet[(letter_position + cypher_shift) % 26]
            # print(shifted_letter)
            message.append(shifted_letter)
        else:
            message.append(letter)
    print(''.join(message))


def option():
    result = input("Type 'e' to encrypt, type 'd' to decrypt, type 'x' to exit:\n")
    return result


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = option()

while direction != "x":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "e":
        encrypt(text, shift)
    if direction == "d":
        encrypt(text, -shift)
    direction = option()
