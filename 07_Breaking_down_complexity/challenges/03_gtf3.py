# Setze Task 7 - 11 um
from data import get_movie_list
import random
movies = get_movie_list()
already_guessed = []

# Task 7 - Erstelle eine Variable, welche die Anzahl an Versuchen der User*in speichert.
# Die Nutzer*in startet mit 4 Versuchen
# Task 8 - Erstelle eine Variable welche festhält, ob die User*in gewonnen hat.
tries_left = 4
won = False
chosen_movie = random.choice(movies)
chosen_movie_length = len(chosen_movie)

covered_movie = []
allowed_symbols = [" ", ":", "-", "\'", "ä", "ö", "ü", "ß", "&", "!", "?"]
for pos in range(chosen_movie_length):
    if chosen_movie[pos] in allowed_symbols:
        covered_movie.append(chosen_movie[pos])
    else:
        covered_movie.append("_")

print(chosen_movie)
print("".join(covered_movie))

# Task 9 - Erstelle eine Schleife, die die User*in so lange zu neuen Eingaben auffordert,
# bis sie entweder keine Versuche mehr oder die Lösung erraten hat

while tries_left > 0 and won is False:
    user_guess = input("Wähle einen Buchstaben: ").lower()

    # Task 10 - Führe das Aufdecken des Buchstaben nur aus, wenn wir den Buchstaben noch nicht geraten haben
    # und dieser auch im Titel vorkommt.
    # Ziehe andernfalls einen Versuch ab
    if user_guess not in already_guessed and user_guess in chosen_movie.lower():
        already_guessed.append(user_guess)

        for pos in range(0, chosen_movie_length):
            if chosen_movie[pos].lower() == user_guess:
                covered_movie[pos] = chosen_movie[pos]

        covered_movie_string = "".join(covered_movie)
        if "_" not in covered_movie:
            won = True
    else:
        tries_left -= 1
        print(f"Das war leider falsch. Du hast noch {tries_left} Versuche")

    # Task 11 - Prüfe, ob die User*in gewonnen hat
    if won:
        print(chosen_movie)
        print("Super, du hast es gelöst!")
    elif tries_left == 0:
        print("Schade, du hast es leider nicht geschafft!")
        print(f"Die richtige Lösung war: {chosen_movie}")
    else:
        print("".join(covered_movie))

    # Task 12 - Wenn die User*in gewonnen oder verloren hat, wird Sie gefragt, ob Sie eine neue Runde spielen möchte
    if won or tries_left == 0:
        answer = input("Möchtest du noch eine Runde spielen (J/N)?\n")
        if answer.lower() == "j":
            already_guessed = []
            tries_left = 4
            won = False
            chosen_movie = random.choice(movies)
            chosen_movie_length = len(chosen_movie)

            covered_movie = []
            for pos in range(chosen_movie_length):
                if chosen_movie[pos] in allowed_symbols:
                    covered_movie.append(chosen_movie[pos])
                else:
                    covered_movie.append("_")
            print("".join(covered_movie))





