# Pay Roulette
# Schreibe ein Programm welches zufällig aus der Liste an Gästen einen auswählt,
# der die Rechnung zahlt. Gehe dazu wie folgt vor:
# Nimm eine Eingabe von Namen, mit Komma getrennt ("Hans, Magerete") via input() an
# Teile dann die den String in eine Liste auf
# Wähle dann, mithilfe von random eine Person aus, welche die Rechnung zahlt.
# Gebe dann mit einem f-String das Ergebnis aus
# Dein Code nach dieser Zeile
import random

names = input("Wer spielt mit?\n")
name_list = names.split(", ")

player_count = len(name_list)
player_pos = random.randint(0, player_count-1)
payer = name_list[player_pos]
# payer = random.choice(name_list)
print(f"Glückwunsch {payer}! Du darfst die Rechnung übernehmen.")


