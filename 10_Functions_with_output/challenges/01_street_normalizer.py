# Schreibe eine Funktion normalize_street_name(name) welche den Straßennamen nach folgenden Regeln normiert
# * Endet der Name mit dem Wort Straße, Weg oder Allee, so muss dieses als eigenes Wort abgetrennt werden
#   * str bzw str. wird du strasse
#      => Wattenbergstraße => Wattenberg Straße
#   * aus ß wird ss
#   * Jedes Wort startet mit Großbuchstaben
#      => https://docs.python.org/3/library/stdtypes.html?highlight=title#str.title


def normalize_street_name(name):
    if name.endswith("str."):
        name = name[:-4] + " strasse"
    elif name.endswith("str"):
        name = name[:-3] + "strasse"
    elif name.endswith("weg"):
        name = name[:-3] + " weg"
    elif name.endswith("allee"):
        name = name[:-5] + " allee"

    name = name.replace("ß", "ss")
    name = name.title()

    return name


print(normalize_street_name("Wattenbergstr."))
print(normalize_street_name("Stannerallee"))
print(normalize_street_name("Straussenberg weg"))
print(normalize_street_name("straße des friedens"))
