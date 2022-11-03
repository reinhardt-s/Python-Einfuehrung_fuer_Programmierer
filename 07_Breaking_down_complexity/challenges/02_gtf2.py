from data import get_movie_list
import random
movies = get_movie_list()
already_guessed = []
# TODO-1 Wähle einen zufälligen Film aus der Liste movies und weise diesen der Variable chosen_movie zu
chosen_movie = random.choice(movies)

# TODO-2 Lass die User*in einen Buchstaben raten. Speichere die Eingabe im Lower-Case in der Variable user_guess
user_guess = input("Wähle einen Buchstaben: ").lower()

# TODO-3 Füge den Buchstaben einer neuen Liste (already_guessed) von Buchstaben die bereits geraten wurden hinzu.
if user_guess not in already_guessed:
    already_guessed.append(user_guess)

# TODO-4 Prüfe, ob der Buchstabe im Film vorkommt
if user_guess in chosen_movie.lower():
    print("Buchstabe ist Teil des Titels")
else:
    print("Buchstabe ist nicht Teil des Titels")

