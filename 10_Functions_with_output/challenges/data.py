# Quelle: https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Deutschen_Bundestages_(19._Wahlperiode)
representatives = []


def load_representative():
    file = open(file="./data.txt", mode="r", encoding="utf-8")
    for representative in file:
        split = representative.split("\t")
        representatives.append({"name": split[0], "year": int(split[1][:-1])})


def get_list_of_representatives():
    if len(representatives) == 0:
        load_representative()
    return representatives

