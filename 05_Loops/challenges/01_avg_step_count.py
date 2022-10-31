# Schreibe eine App, in welche die User*in ihre Schrittzahlen der letzten n Tage eingeben kann
# Die App berechnet daraus das arithmetische Mittel https://de.wikipedia.org/wiki/Mittelwert#Arithmetischer_Mittelwert
# Nutze hierbei die sum() Funktion um die Werte aufzusummieren.
# Beachte, dass du Integer und keine String aufsummieren willst
# Gib abschließend das Ergebnis gerundet und ohne Nachkommastellen aus

step_counts_string = input("Bitte gib mit Komma getrennt, deine Schrittzahlen pro Tag ein: ")
step_count_list = step_counts_string.split(",")

# Dein Code nach dieser Zeile

# for steps_pos in range(0, len(step_count_list)):
#     step_count_list[steps_pos] = int(step_count_list[steps_pos])
# steps_sum = sum(step_count_list)

steps_sum = 0
for steps in step_count_list:
    steps_sum += int(steps)

avg = round(steps_sum / len(step_count_list))
print(f"Du läufst durchschnittlich {avg} Schritte am Tag.")

