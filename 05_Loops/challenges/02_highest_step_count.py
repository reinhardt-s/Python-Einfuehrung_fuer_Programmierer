# Schreibe eine App, in welche die User*in ihre Schrittzahlen der letzten n Tage eingeben kann
# Die App gibt dann aus, welches die höchste Anzahl an gelaufenen Schritten war

step_counts_string = input("Bitte gib mit Komma getrennt, deine Schrittzahlen pro Tag ein: ")
step_count_list = step_counts_string.split(",")

# Dein Code nach dieser Zeile

# for steps_pos in range(0, len(step_count_list)):
#     step_count_list[steps_pos] = int(step_count_list[steps_pos])
# print(max(step_count_list))

highest_step_count = 0
for steps in step_count_list:
    steps_int = int(steps)
    if steps_int > highest_step_count:
        highest_step_count = steps_int

print(f"Du hast an deinem besten Tag {highest_step_count} Schritte gemacht.")
