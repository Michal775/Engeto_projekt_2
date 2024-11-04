"""
projekt_2b.py: druhý projekt do Engeto Online Python Akademie

"Tic-tac-toe" hra

author: Michal Szotkowski
email: michal.szotkowski@molnlycke.com
discord: Michal S. misande
"""

# Pozdrav a pravidla hry
print("Welcome to Tic Tac Toe")
oddelovac = "=" * 25
print(oddelovac)
print(
"""GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of thir
marks in a:
* horizontal,
* vertical or
* diagonal row"""
)
print(oddelovac)
print("Let's start the game")
print(oddelovac)

# Vytvoření prázdného hracího pole
pole = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Design hracího pole
def hraci_pole():
    cara = "+---+---+---+"
    print(cara)
    for radek in pole:
        print(f"| {radek[0]} | {radek[1]} | {radek[2]} |")
        print(cara)

# Kontrola výhry
def kontrola_vyhry():
    # Kontrola výhry v řádcích
    for radek in pole:
        if radek[0] == radek[1] == radek[2] != " ":
            return radek[0]
    # Kontrola výhry ve sloupcích
    for sloupec in range(3):
        if pole[0][sloupec] == pole[1][sloupec] == pole[2][sloupec] != " ":
            return pole[0][sloupec]
    # Kontrola výhry na diagonálách
    if pole[0][0] == pole[1][1] == pole[2][2] != " ":
        return pole[0][0]
    if pole[0][2] == pole[1][1] == pole[2][0] != " ":
        return pole[0][2]
    return None

# Hra
hraci_pole()
hrac = "X"
vyhra = None

while vyhra is None:
    radek = int(input(f"Player {hrac}, please enter row number (1, 2, 3): ")) - 1
    sloupec = int(input(f"Player {hrac}, please enter column number (1, 2, 3): ")) - 1

    if pole[radek][sloupec] == " ":
        pole[radek][sloupec] = hrac
        hraci_pole()
        vyhra = kontrola_vyhry()
        if vyhra is None:
            hrac = "O" if hrac == "X" else "X"
    else:
        print("This field is already taken. Please choose another one.")

if vyhra == "X":
    print("Congratulations, the player X won!")
elif vyhra == "O":
    print("Congratulations, the player O won!")
else:
    print("It's a tie!")

input("Press Enter to exit...")

# Konec programu
