# Schreibe ein Spiel, das folgende Anforderungen erfüllt:
# * Das Spiel fragt nach dem Schwierigkeitsgrad
# * Im Easy Mode hat die Spieler*in 10 versuche, im Hard Mode 5
# * Die Spieler*in muss eine Zufallszahl zwischen 1 und 100 erraten
# * Die Spieler*in verliert, wenn Sie nach 5/10 versuchen die Zahl nicht erraten hat
# * Nachdem ein Spiel gewonnen oder verloren wurde, wird erneut gefragt, ob die Spieler*in spielen mag
# * Der Computer gibt Hinweise, ob die Eingabe der Spieler*in zu hoch oder zu tief ist

import random

ATTEMPTS_EASY = 10
ATTEMPTS_HARD = 5

WON = "Großartig! Du hast gewonnen!"
LOST = "Das hat wohl nicht geklappt. Vie Glück beim nächsten Mal."
TOO_HIGH = "Nee, das ist zu hoch."
TOO_LOW = "Uff, das ist zu wenig."
GUESS_PROMPT = "Rate die Zahl: "
PLAY_GAME_PROMPT = "Möchtest du Guess The Number spielen? J/N\n"
MODE_PROMPT = "Möchtest du den (E)asy-Mode oder (H)ard-Mode spielen?\n"

number_to_guess = -1


def play_game(attempts):
    if attempts == 0:
        print(LOST)
        return
    guess = int(input(GUESS_PROMPT))
    if guess == number_to_guess:
        print(WON)
        return
    elif guess > number_to_guess:
        print(TOO_HIGH)
        attempts -= 1
    else:
        print(TOO_LOW)
        attempts -= 1
    return play_game(attempts)


while input(PLAY_GAME_PROMPT).lower() == "j":
    choice = input(MODE_PROMPT).lower()
    if choice == "e":
        attempts = ATTEMPTS_EASY
    else:
        attempts = ATTEMPTS_HARD

    number_to_guess = random.randint(1, 100)
    play_game(attempts)

