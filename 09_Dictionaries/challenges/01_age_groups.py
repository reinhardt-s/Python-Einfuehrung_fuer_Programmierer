# Schreibe ein Programm, welches das Alter der Läufer gegen Ihre Altersklasse austauscht:
# * "U20" 19/18 Jahre
# * "Läufer*innen"    20-29 Jahre
# * "Senior*innen 30" 30-34 Jahre
# * "Senior*innen 35" 35-39 Jahre
# * "Senior*innen 40" 40-44 Jahre
# * "Senior*innen 45" 45-49 Jahre
# * "Senior*innen 50" 50-54 Jahre


runners = {
    "Tobias": 43,
    "Hanna": 21,
    "Bettina": 31,
    "Horst": 44,
    "Lena": 19,
    "Erwin": 52,
    "Sigried": 44,
    "Sven": 20
}

print(runners)
# Dein Code nach dieser Zeile

for name in runners:
    if runners[name] == 18 or runners[name] == 19:
        runners[name] = "U20"
    elif 20 <= runners[name] <= 29:
        runners[name] = "Läufer*innen"
    elif 30 <= runners[name] <= 34:
        runners[name] = "Senior*innen 30"
    elif 35 <= runners[name] <= 39:
        runners[name] = "Senior*innen 35"
    elif 40 <= runners[name] <= 44:
        runners[name] = "Senior*innen 40"
    elif 45 <= runners[name] <= 49:
        runners[name] = "Senior*innen 45"
    elif 50 <= runners[name] <= 54:
        runners[name] = "Senior*innen 50"

# Dein Coder über dieser Zeile
print(runners)
