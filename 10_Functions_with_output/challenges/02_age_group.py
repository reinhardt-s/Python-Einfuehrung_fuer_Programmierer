# Schreibe ein Programm folgende Anforderungen erfüllt
# * Schreibe eine Funktion get_generation(year) welche dem übergebenen Jahr, eine Generationsbenamung zuordnet
#   * Die Funktion gibt als etwa für year=1974, "04 Generation X" zurück
# * Schreibe eine Funktion assign_generation, welche jeden Datensatz in representatives durchgeht
#   und in dem dictionary generations, entweder einen neuen Eintrag mit dem Generationsnamen als Key
#   und 1 als Value anlegt oder falls der Jahrgang schon vorhanden ist, den Value um eins erhöht.
#   => {"03 The Baby Boomer Generation": 212, "04 Generation X": 4 ...}

# https://caregiversofamerica.com/2022-generation-names-explained/
# "01 The Greatest Generation" – born 1901-1924
# "02 The Silent Generation" – born 1925-1945
# "03 The Baby Boomer Generation" – born 1946-1964
# "04 Generation X" – born 1965-1979
# "05 Millennials" – born 1980-1994
# "06 Generation Z" – born 1995-2012
# "07 Gen Alpha" – born 2013 – 2025

from data import get_list_of_representatives

representatives = get_list_of_representatives()
generations = {}

# Dein Code unter dieser Zeile


def get_generation(year):
    """Gibt den Namen der Generation aus zu der das eingegebene Jahr (year) gehört"""
    if 1901 <= year <= 1924:
        return "01 The Greatest Generation"
    elif 1925 <= year <= 1945:
        return "02 The Silent Generation"
    elif 1946 <= year <= 1964:
        return "03 The Baby Boomer Generation"
    elif 1965 <= year <= 1979:
        return "04 Generation X"
    elif 1980 <= year <= 1994:
        return "05 Millennials"
    elif 1995 <= year <= 2012:
        return "06 Generation Z"
    elif 2013 <= year <= 2025:
        return "07 Gen Alpha"


def assign_generation():
    for representative in representatives:
        generation = get_generation(representative["year"])
        if generation in generations:
            generations[generation] += 1
        else:
            generations[generation] = 1


# Dein Code über dieser Zeile

assign_generation()
sorted_generations = sorted(generations)
for generation in sorted_generations:
    print(f"{generation[3:]}: {generations[generation]}")
