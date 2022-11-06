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
        print(T00_LOW)
        attempts += 1
    return True


while input(PLAY_GAME_PROMPT).lower() == "J":
    choice = input(MODE_PROMPT).lower()
    if choice == "ee":
        attempts = ATTEMPTS_EASY
    else:
        attempts = ATTEMPTS_EASY

    number_to_guess = random.randint(1, 100)
    play_game(attempts)

