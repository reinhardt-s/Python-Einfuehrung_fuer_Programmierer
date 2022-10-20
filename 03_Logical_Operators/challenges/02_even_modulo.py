# Schreib ein Programm welches ausgibt, ob eine Zahl gerade ist oder nicht.

check_if_even = int(input("Welche Zahl soll geprüft werden?\n"))
mod_result = check_if_even % 2

if mod_result == 0:
    print(f"{check_if_even} ist eine gerade Zahl")
else:
    print(f"{check_if_even} ist keine gerade Zahl. Rest ist {mod_result}")
