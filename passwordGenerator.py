import random as rand
import string

symbols = string.punctuation
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
letters = lowerLetters + upperLetters
nums = string.digits
passwordList = []

while True:
    try:
        passLength = int(input("How long do you want you password (8 as a minimum)?"))
        while passLength < 8:
            passLength = input(
                "Password is too short, it would be easily hackable please insert a length higher than 8:")
        if passLength >= 8:
            break
    except ValueError:
        print("The input was not a valid integer.")

while True:
    try:
        passStrength = int(input("What do you want your password to consist of?\n Input 0 for only upper and lower letters\n Input 1 for both upper and lower case letters and numbers\n Input 2 for all letter,symbols and numbers."))
        while passStrength > 2:
            passStrength = input(
                "Incorrect input. Please enter a number between 0 and 2")
        if passStrength <= 2:
            break
    except ValueError:
        print("The input was not a valid integer.")

def passwordGenerator(passStrength, passLength):
    if passStrength == 0:
        password = rand.sample(letters, passLength)

    if passStrength == 1:
        strength1 = letters+nums
        password = rand.sample(strength1, passLength)

    if passStrength == 2:
        all = letters+nums+symbols
        password = rand.sample(all, passLength)

    password = "".join(password)
    return password

print(passwordGenerator(passStrength, passLength))
