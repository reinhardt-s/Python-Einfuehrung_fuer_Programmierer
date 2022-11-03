# Schreibe ein Programm, welches per Zufall "Kopf" oder "Zahl" ausgibt
# Benutze hierzu das Random Modul und generiere damit entweder einer 1 oder eine 0
# 1 = Kopf
# 0 = Zahl

import random

result = random.randint(0, 1)
if result == 1:
    print("Kopf")
else:
    print("Zahl")
