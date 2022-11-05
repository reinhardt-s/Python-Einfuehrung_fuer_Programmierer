# Schreibe eine App die es Ron erlaubt, in seinem Zauberspruchbuch
# * Einen vorhandenen Eintrag anzuzeigen
# * Alle vorhandenen Zauberspruchnamen auszugeben
# * Einen neuen Zauberspruch einzutragen
# * Einen Zauberspruch zu entfernen
# * Nach dem das Programm die gweünschte Aufgabe erledigt hat, soll es erneut Fragen, welche Aktion ausgeführt werden
#   soll, bis die Nutzer*in sich entscheidet das Programm zu verlassen

spells = {
    "Expelliarmus": "Entwaffnungszauber",
    "Lumos": "Beleuchtungszauber",
    "Wingardium Leviosa": "Schwebezauber",
    "Accio": "Aufrufezauber",
    "Nox": "Verdunklungszauber"
          }


def find_spell(spell_name):
    if spell_name in spells:
        print(f"{spell_name} ist ein {spells[spell_name]}")
    else:
        print("Diesen Zauberspruch kenne ich nicht.")


def add_spell():
    spell_name = input("Wie heißt der Zauberspruch den du hinzufügen möchtest?\n")
    spell_kind = input(f"Was für ein Zauber ist {spell_name}?\n")
    spells[spell_name] = spell_kind


def remove_spell(spell_name):
    if spell_name in spells:
        spell_kind = spells.pop(spell_name)
        print(f"Ich habe den Zauberspruch {spell_name} vom Typ {spell_kind} wieder gestrichen.")
    else:
        print("Diesen Zauberspruch kenne ich nicht.")


def index():
    for spell_name in sorted(spells):
        print(spell_name)


action = ""
while action != "v":
    action = input("Hi Ron! Möchtest du \n* einen Zauber (n)achschlagen, \n* einen (e)rgänzen, "
                   "\n* im (I)nhaltsverzeichnis blättern,\n* einen Zauberspruch (l)öschen"
                   "\n* oder das Programm (v)erlassen?\n").lower()
    if action == "n":
        name = input("Wie heißt der Zauberspruch?\n")
        find_spell(name)
    elif action == "e":
        add_spell()
    elif action == "i":
        index()
    elif action == "l":
        name = input("Wie heißt der Zauberspruch?\n")
        remove_spell(name)
    else:
        print("Tut mir leid, das habe ich nicht verstanden.")
print("Auf wiedersehen")

