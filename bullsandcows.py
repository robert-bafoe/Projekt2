import random
ODDELOVAC = 65 * "-"
PRAVIDLA = """
Discover the hidden code!
Bulls = correct code, correct position.
Cows = correct code, wrong position.
"""
print(f"Welcome to BULLS AND COWS GAME!")
print(ODDELOVAC)
JMENO = input("Enter your name: ")
ZNASPRAVIDLA = input(f"Hello {JMENO}, do you know the rules of this game? ( Y / N ): ")

if ZNASPRAVIDLA == "N":
    print(ODDELOVAC)
    print(f"{PRAVIDLA}")
    print(ODDELOVAC)
else:
    print(ODDELOVAC)

TAJNYKOD = [random.randint(0,9) for n in range(4)]

print(f"I've generated a random 4 digit number for you. {TAJNYKOD}")
print(f"Let's play!")
print(ODDELOVAC)

POKUS = 0
while True:
    POKUS += 1

    TIP = [int(i) for i in str(input(f"Enter a 4 digit number (guess #{POKUS}): "))]

    # while len(TIP) != 4 or (not TIP.isdigit()):
    #     print('Not a 4 digit number')
    #     TIP = [int(i) for i in str(input(f"Enter a 4 digit number (guess #{POKUS}): "))]

    if TIP == TAJNYKOD:
        print(f"CORRECT! You've guessed the right number in {POKUS} guesses!")
        break

    else:
        COWS = 0
        BULLS = 0

        for x in range(0,4):
            if TIP[x] == TAJNYKOD[x]:
                BULLS += 1
            elif TIP[x] in TAJNYKOD:
                COWS += 1

    print(f"bulls: {BULLS}, cows: {COWS}")
    print(ODDELOVAC)