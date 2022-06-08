# Save the input in this variable
ticket = "090234"
digits = [int(num) for num in str(ticket)]


# Add up the digits for each half
half1 = sum(digits[0:2])
half2 = sum(digits[-3::])

print(half1,half2)
# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
