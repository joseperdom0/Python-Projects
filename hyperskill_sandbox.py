number = str(input())
text_to_speech = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for digit in number:
    print(text_to_speech[int(digit)])
