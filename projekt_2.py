"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

"Bulls & Cows" hra

author: Michal Szotkowski
email: michal.szotkowski@molnlycke.com
discord: Michal S. misande
"""
import random

# Pozdrav uživatele
oddelovaci_cara = "-" * 40
print(f"""Hi there!,
{oddelovaci_cara}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{oddelovaci_cara}""")

# Vygenerování tajného čtyřmístného čísla, které nesmí začínat 0 a bez duplicitních číslic
tajne_cislo = str(random.randint(1000, 9999))
while len(set(tajne_cislo)) < 4:
    tajne_cislo = str(random.randint(1000, 9999))

# funkce na množné číslo bull/cow
def uprav_mnozne_cislo(pocet: int, slovo: str) -> str:
    """
    Funkce přidá 's' na konec slova, pokud se pocet nerovná 1.

    :Example:
    >>> vysledek = uprav_mnozne_cislo(1, "bull")
    >>> vysledek
    '1 bull'
    >>> vysledek = uprav_mnozne_cislo(2, "cow")
    >>> vysledek
    '2 cows'
    """
    if pocet == 1:
        return f"{pocet} {slovo}"
    else:
        return f"{pocet} {slovo}s"

# Hra
pocet_pokusu = 1
while True:
    bulls = 0
    cows = 0
    tip_uzivatele = input("Enter a number: ")
    if len(tip_uzivatele) != 4:     # Kontrola délky čísla
        print("Your number has to be 4 digits long.")
    elif not tip_uzivatele.isdigit():       # Kontrola, zda se jedná o číslo
        print("Your number has to be a number.")
    elif tip_uzivatele[0] == "0":       # Kontrola, zda číslo nezačíná 0
        print("Your number can't start with 0.")
    elif len(set(tip_uzivatele)) < 4:       # Kontrola, zda číslo nemá duplicitní číslice
        print("Your number can't have duplicate digits.")
    else:
        for i in range(4):
            if tip_uzivatele[i] == tajne_cislo[i]:
                bulls += 1
            elif tip_uzivatele[i] in tajne_cislo:
                cows += 1
        print(f"{uprav_mnozne_cislo(bulls, "bull")}, {uprav_mnozne_cislo(cows, "cow")}")
        print(oddelovaci_cara)
        if bulls == 4:
            print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses!")
            print(oddelovaci_cara)
            break
        pocet_pokusu += 1

input("Press Enter to exti...") # Ukončení programu



