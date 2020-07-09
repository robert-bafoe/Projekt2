import random
import time

ODDELOVAC = 65 * "-"
PRAVIDLA = """Discover the hidden code!
Bulls = correct code, correct position.
Cows = correct code, wrong position."""
print(f"Welcome to BULLS AND COWS GAME!")
print(ODDELOVAC)
JMENO = input("Enter your name: ")
ZNASPRAVIDLA = input(f"Hello {JMENO}, do you know the rules of this game? ( y / n ): ")

if ZNASPRAVIDLA == "N" or ZNASPRAVIDLA == "n":
    print(ODDELOVAC)
    print(f"{PRAVIDLA}")
    print(ODDELOVAC)
    READY = input(f"So, {JMENO}, are you ready now? ( y / n ): ")
    if READY == "N" or READY == "n":
        print(f"Well, bye then.")
        exit()
else:
    print(ODDELOVAC)

TAJNYKOD = [random.randint(0,9) for n in range(4)]

print(f"I've generated a random 4 digit number for you. {TAJNYKOD}")
print(f"Let's play!")
print(ODDELOVAC)
ZACATEK = time.time()

POKUS = 0
while True:
    POKUS += 1

    TIP = [int(i) for i in str(input(f"Enter a 4 digit number (guess #{POKUS}): "))]

    if TIP == TAJNYKOD:
        KONEC = time.time()
        print(f"CORRECT! You've guessed the right number in {POKUS} guesses and in {round(KONEC - ZACATEK)} seconds!")

        if POKUS == 1:
            print("WOW! That is unbelieveble!")
        elif POKUS < 3:
            print("GREAT! That is amazing!")
        elif POKUS < 5:
            print("COOL! That is great!")
        elif POKUS < 10:
            print("WELL! Not so bad!")
        else:
            print("hmmm.. what else to say..")

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