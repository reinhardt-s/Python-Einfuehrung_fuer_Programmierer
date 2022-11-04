# Setze Task 5 - 6 um
from data import get_movie_list
import random
movies = get_movie_list()
already_guessed = []

chosen_movie = random.choice(movies)
chosen_movie_length = len(chosen_movie)
# Task 5 Erstelle eine Liste mit "_" korrespondierend zu der Anzahl an Buchstaben
# Der Unterstrich soll nur gesetzt werden, wenn es sich nicht, um eines der erlaubten Symbole (allowed_symbols) handelt
# Diese Symbole sollen direkt, statt dem Unterstrich angezeigt werden:
# " ", ":", "-", "\'", "ä", "ö", "ü", "ß", "&", "!", "?"

# covered_movie = ["_" for letter in chosen_movie]
# oder
# covered_movie = ["_"] * chosen_movie_length

covered_movie = []
allowed_symbols = [" ", ":", "-", "\'", "ä", "ö", "ü", "ß", "&", "!", "?"]
for pos in range(chosen_movie_length):
    if chosen_movie[pos] in allowed_symbols:
        covered_movie.append(chosen_movie[pos])
    else:
        covered_movie.append("_")

print(chosen_movie)

user_guess = input("Wähle einen Buchstaben: ").lower()


if user_guess not in already_guessed:
    already_guessed.append(user_guess)

# Task 6 tausche bei einem Treffer den entsprechenden Unterstrich durch den passenden Buchstaben aus
for pos in range(0, chosen_movie_length):
    if chosen_movie[pos].lower() == user_guess:
        covered_movie[pos] = chosen_movie[pos]
    else:
        print("Wrong")

print("".join(covered_movie))
