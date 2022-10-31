# Schreibe eine App, welche die User*in fragt, was sie wählt: 1: Stein, 2: Schere, 3: Papier, 4: Echse, 5: Spock
# Die App wählt dann per Pseudozufallszahl ebenfalls eine Hand aus.
# Nach den Regeln von http://www.samkass.com/theories/RPSSL.html wird nun die Gewinner*in
# ermittelt:
# - Schere schneidet Papier
# - Papier umwickelt Stein
# - Stein trifft Echse
# - Echse vergiftet Spock
# - Spock zertrümmert Schere
# - Schere zerlegt Echse
# - Echse isst Papier
# - Papier widerlegt Spock
# - Spock vaporisiert Stein
# - Stein zerstört Schere
# Beachte bei der Entwicklung auch Grenzfälle:
# - App und User*in wählen die gleiche Hand
# - User*in macht ungültige eingabe
# Zeige jeweils, nachdem die User*in und die App Ihre Hand gewählt haben, die ASCII art zur Hand an.
# Benutze hierzu aus images.py die Liste hands

# dein Code nach dieser Zeile
import images
import random

print("Willkommen bei Rock Paper Scissors Lizard Spock!")


user_choice = int(input("Wähle deine Hand:\n1: Stein, 2: Schere, 3: Papier, 4: Echse, 5: Spock: "))
print(f"Du wählst: {images.hands[user_choice-1]}")
app_choice = random.randint(1, 5)
print(f"Computer wählt: {images.hands[app_choice-1]}")

if user_choice == app_choice:
    print("Unentschieden!")
elif user_choice == 2:  # Schere
    if app_choice == 3 or app_choice == 4:  # Papier / Echse
        print("Du gewinnst!")
    else:
        print("Du verlierst")
elif user_choice == 3:  # Papier
    if app_choice == 1 or app_choice == 5:  # Stein / Spock
        print("Du gewinnst!")
    else:
        print("Du verlierst")
elif user_choice == 1:  # Stein
    if app_choice == 4 or app_choice == 2:  # Echse / Schere
        print("Du gewinnst!")
    else:
        print("Du verlierst")
elif user_choice == 4:  # Echse
    if app_choice == 5 or app_choice == 3:  # Spock / Papier
        print("Du gewinnst!")
    else:
        print("Du verlierst")
elif user_choice == 5:  # Spock
    if app_choice == 2 or app_choice == 1:  # Schere / Stein
        print("Du gewinnst!")
    else:
        print("Du verlierst")
else:
    print("Keine gültige Eingabe. Du verlierst")
