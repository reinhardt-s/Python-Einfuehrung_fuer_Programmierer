# Schreibe eine App, welche folgende Aufgaben erfüllt:
# Task-1: Erstelle eine Funktion ask_for_data, welche folgende Informationen erfragt:
#           * Frage die Nutzer*in, ob diese (V)erschküsseln oder (E)ntschlüsseln möchte
#           * Frage die Nutzer*in, wie viele Zeichen verschoben wird, bzw. wurde.
#           * Frage die Nutzer*in, wie die Nachricht lautet
#           * Rufe die Funktion crypt mit den Argumenten auf.
# Task-2: Schreibe eine Funktion crypt welche:
#           * die oben genannten Argumente annimmt
#           * je nachdem ob es sich um eine Ver- oder Ent-schlüsselung handelt,
#             die Nachricht in die eine oder andere Richtung verschiebt
# Task-3: Rufe ask_for_data auf.
# Task-4: Nachdem Die (Ent-)Schlüsselung beendet wurde, fragt das Programm,
#         ob ein weiterer Durchlauf gestartet werden soll
# Tipps:
# * Du kannst mit einer Liste an vorgegebenen Buchstaben arbeiten
# * Herausforderung: Du kannst auch mit Unicode arbeiten:
# * Nutze hierzu die chr-Funktion -> https://docs.python.org/3/library/functions.html#chr
# * https://en.wikipedia.org/wiki/List_of_Unicode_characters


def ask_for_data():
    method = input("Soll (V)erschlüsselt oder (E)ntschlüsselt werden?\n").lower()
    shift = int(input("Wie groß ist die Verschiebung?\n"))
    message = input("Wie lautet die Nachricht?\n")
    crypt(method, shift, message)


def crypt(method, shift, message):
    output = ""
    if method != "v":
        shift *= -1
    for letter in message:
        pos = ord(letter) + shift
        if pos > 1114111:
            pos = pos - 1114111
        elif pos < 0:
            pos = 1114111 + pos

        output += chr(pos)

    print(f"Nachricht: {output}")


while input("Möchten Sie das Programm starten(J/N)?\n").lower() == "j":
    ask_for_data()
