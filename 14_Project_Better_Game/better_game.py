import random

from data import get_list_of_games

GAMES = get_list_of_games()

# Dein Code nach dieser Zeile
# Schreibe ein Spiel, welches folgende Anforderungen erfüllt
# Du benutzt die Daten aus der Variable GAMES
# Die Spieler*in wir, gefragt ob sie eine Runde Better Game spielen will.
# Sie wird jedes Mal erneut gefragt, wenn das Spiel geendet hat.
# Der Spieler*in werden zwei Zufällig gewählte Spiele präsentiert, wobei vermieden werden muss,
# dass zwei Mal das selbe Spiel gewählt wurde.
# Die Spieler*in wir aufgefordert zu raten, welches Spiel mehr positive Bewertungen hat.
# Hat sie Spieler*in richtig getippt, erhält sie einen Punkt.
# Wenn nicht endet das Spiel.
# Jedes Mal, der Spielerin mitgeteilt wird, ob sie richtig geraten hat, wird auch angezeigt,
# wie oft sie schon richtig lag.


WON = "Das war richtig! Super!"
LOST = "Das hat wohl nicht geklappt. Viel Glück beim nächsten Mal."
GUESS_PROMPT = "Welches hat mehr positive Bewertungen?"
PLAY_GAME_PROMPT = "Möchtest du Better Game spielen? J/N\n"


def get_games():
    games = {"left": random.choice(GAMES)}
    smaller_list = GAMES
    smaller_list.remove(games["left"])
    games["right"] = random.choice(smaller_list)
    return games


def play_game(streak):
    games = get_games()
    choice = input(f"{GUESS_PROMPT} (1) - {games['left']['game']} oder (2) - {games['right']['game']}?")

    if (choice == "1" and games['left']['positiv-ratings'] > games['right']['positiv-ratings']) \
            or (choice == "2" and games['right']['positiv-ratings'] > games['left']['positiv-ratings']):
        print(f"{WON} - Deine Streak: {streak + 1}")
        play_game(streak+1)
    else:
        print(f"{LOST} - Deine Streak: {streak}")
        return


while input(PLAY_GAME_PROMPT).lower() == "j":
    play_game(0)

