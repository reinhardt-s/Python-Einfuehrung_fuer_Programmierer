# Schreibe eine App, welche ein Passwort nach folgenden Regeln erstellt:
# Frage die Nutzer*in nacheinaner
#  - wie viele Sonderzeichen
#  - wie viele Zahlen
#  - wie viel Buchstaben (groß und klein)
# ihr Passwort haben soll
# Wähle dann per Pseudozufallszahlen aus den entsprechenden Listen, zeichen in gewünschter Menge aus und kombiniere
# diese zu einem Passwort. Zeige die dass an.

letters = ["Q", "q", "W", "w", "E", "e", "R", "r", "T", "t", "Z", "z", "U", "u", "I", "i", "O", "o", "P", "p", "A", "a",
           "S", "s", "D", "d", "F", "f", "G", "g", "H", "h", "J", "j", "K", "k", "L", "l", "Y", "y", "X", "x", "C", "c",
           "V", "v", "B", "b", "N", "n", "M", "m"]

symbols = ["!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "-", "_", ":", ".", ";", ",", "<", ">", "|", "µ",
           "}", "{", "[{]", "]", "\\"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Dein Code nach dieser Zeile
import random

num_letters = int(input("Wie viele Buchstaben soll dein Passwort haben: "))
num_numbers = int(input("Wie viele Zahlen soll dein Passwort haben: "))
num_symbols = int(input("Wie viele Sonderzeichen soll dein Passwort haben: "))

password = []

for count in range(0, num_letters):
    password.insert(random.randint(0, len(password)), random.choice(letters))

for count in range(0, num_numbers):
    password.insert(random.randint(0, len(password)), random.choice(numbers))

for count in range(0, num_symbols):
    password.insert(random.randint(0, len(password)), random.choice(symbols))

print("".join(password))
# random.shuffle(password)
# print("".join(password))
