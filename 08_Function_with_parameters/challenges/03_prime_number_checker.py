# Schreibe eine App, die die Nutzer*in dazu auffordert eine Zahl einzugeben
# Schreibe eine Funktion names check_for_prime, welche ausgibt, ob es eine Primzahl ist oder nicht
# Tipps:
# Du kannst mit Modulo arbeiten
# Primzahlen sind nur durch 1 und sich selbst teilbar

def check_for_prime(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime:
        print(f"{number} ist eine Primzahl")
    else:
        print(f"{number} ist keine Primzahl")


n = int(input("Welche Zahl soll geprüft werden?\n"))
check_for_prime(n)