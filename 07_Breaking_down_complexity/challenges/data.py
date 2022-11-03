import random

movies = []


def load_movies():
    file = open("../movies.txt", "r")
    for movie in file:
        movies.append(movie[:-1])


def get_movie_list():
    if len(movies) == 0:
        load_movies()
    return movies
