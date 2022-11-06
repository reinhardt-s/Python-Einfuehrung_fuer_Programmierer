# Quelle: https://steamdb.info/stats/gameratings/
games = []


def load_games():
    file = open(file="./data.txt", mode="r", encoding="utf-8")
    for representative in file:
        split = representative.split("\t")
        games.append({"game": split[0], "positiv-ratings": int(split[1][:-1])})


def get_list_of_games():
    if len(games) == 0:
        load_games()
    return games

