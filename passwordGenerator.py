import random as rand

symbols = list(":,.~`/'[]=-+_()*&^%$#@!")
letters = list("abcdefghijklmnopqrstuvwxyz")
nums = list("0123456789")
passwordList = []

while True:
    try:
        passLength = input("How long do you want you password (8 as a minimum)?")
        while int(passLength) < 8:
            passLength = input(
                "Password is too short, it would be easily hackable please insert a length higher than 8:")
        if int(passLength) >= 8:
            break
    except ValueError:
        print("The input was not a valid integer.")

while True:
    try:
        passStrength = input("What do you want your password to consist of?\n Input 0 for only letters\n Input 1 for both upper and lower case letters and numbers\n Input 2 for all letter,symbols and numbers.")
        while int(passStrength) > 2:
            passStrength = input(
                "Incorrect input. Please enter a number between 0 and 2")
        if int(passStrength) <= 2:
            break
    except ValueError:
        print("The input was not a valid integer.")

def passwordGenerator(passStrength, passLength):
    if int(passStrength) == 0:
        for i in range(int(passLength)):
            passwordList.append(rand.choice(letters))

    if int(passStrength) == 1:
        ratio = rand.randint(2, int(passLength)-2)

        for i in range(ratio):
            if rand.randint(1,2) == 1:
                passwordList.append(rand.choice(letters).upper())
            else:
                passwordList.append(rand.choice(letters))

        for i in range(ratio, int(passLength)):
            passwordList.append(rand.choice(nums))

    if int(passStrength) == 2:
        ratioNum = rand.randint(2, int(passLength) - 2)
        ratioSym = rand.randint(2, int(passLength) - 2)

        while ratioNum + ratioSym > int(passLength):
            ratioNum = rand.randint(2, int(passLength) - 2)
            ratioSym = rand.randint(2, int(passLength) - 2)

        if ratioNum > ratioSym:
            tmp = ratioSym
            ratioSym = ratioNum
            ratioLet = tmp

        for i in range(ratioLet):
            passwordList.append(rand.choice(nums))

        for i in range(ratioLet, ratioSym):
            passwordList.append(rand.choice(symbols))

        for i in range(ratioSym, int(passLength)):
            if rand.randint(1, 2) == 1:
                passwordList.append(rand.choice(letters).upper())
            else:
                passwordList.append(rand.choice(letters))

    rand.shuffle(passwordList)
    password = "".join(passwordList)
    return password

print(passwordGenerator(passStrength, passLength))