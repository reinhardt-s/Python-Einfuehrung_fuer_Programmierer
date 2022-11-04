# Setze Task 1 - 4 um


from data import get_movie_list
import random
movies = get_movie_list()
already_guessed = []
# Task-1 Wähle einen zufälligen Film aus der Liste movies und weise diesen der Variable chosen_movie zu
chosen_movie = random.choice(movies)
print(chosen_movie)
# Task-2 Lass die User*in einen Buchstaben raten. Speichere die Eingabe im Lower-Case in der Variable user_guess
user_guess = input("Wähle einen Buchstaben: ").lower()

# Task-3 Füge den Buchstaben einer neuen Liste (already_guessed) von Buchstaben die bereits geraten wurden hinzu.
if user_guess not in already_guessed:
    already_guessed.append(user_guess)

# Task-4 Prüfe jede Stelle im Filmtitel auf den eingegebenen Buchstaben,
# Gib dann entsprechen Ja oder Nein aus
for letter in chosen_movie:
    if letter == user_guess:
        print("Right")
    else:
        print("Wrong")

